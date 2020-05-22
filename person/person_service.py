import re
import string
from datetime import datetime
import random
import logging

from generator.generator import generate_values_dynamically
from generator.model.model_datetime import ModelDateTime
from generator.model.model_entity import ModelEntity
from person.models import Person


class PersonService:
    def __init__(self, sourcefile):
        self.descriptions = ModelEntity.parse_model(sourcefile)

    def create_person(self):
        values = self.__generate_values()

        person = Person()
        person.sex = self.__generate_sex(values)
        person.birth_date = self.__generate_date(values)
        person.first_name = self.__generate_name(values, person.sex)
        person.last_name = self.__generate_surname(person.sex)
        person.pesel = self.__generate_pesel(person.birth_date, person.sex)
        person.email = self.__generate_email(person.first_name, person.last_name)
        person.phone = self.__generate_phone()
        person.password = self.__generate_password()
        logging.basicConfig(level=logging.DEBUG)
        logging.info(f"Created person {person.first_name} {person.last_name} with pesel {person.pesel}")
        return person

    def __generate_values(self):
        results = {}

        for desc in self.descriptions:
            key, value = generate_values_dynamically(desc)
            results[key] = value

        return results

    def __generate_date(self, values):
        date_range = values['birth_date_range']
        date = datetime.strptime(values[date_range], ModelDateTime.default_date_format)
        return date

    def __generate_sex(self, values):
        sex = values['sex']
        return sex

    def __generate_name(self, values, sex):
        if sex == 0:
            name = values['female_first_name']
        else:
            name = values['male_first_name']

        return name

    def __generate_surname(self, sex):
        # creating variable
        vowel = ["a", "e", "i", "o", "u", "y"]
        consonants = ["b", "c", "d", "g", "h", "j", "k", "l", "m", "n", "p", "r", "s", "t", "w", "z"]
        male_surname_ends = ["ski", "cki", "dzki", "k", "ki", "wicz", "n", "ny", "l"]
        female_surname_ends = ["ska", "cka", "dzka", "k", "ka", "wicz", "na", "l"]
        surname = ""
        # generating the first 3 letters of surname
        surname = consonants[random.randint(0, len(consonants) - 1)].upper() \
                  + vowel[random.randint(0, len(vowel) - 1)] \
                  + consonants[random.randint(0, len(consonants) - 1)] \
                  + vowel[random.randint(0, len(vowel) - 1)]
            # adding endings basic on sex
        if sex == 1:
            surname = surname + male_surname_ends[random.randint(0, len(male_surname_ends) - 1)]
        else:
            surname = surname + female_surname_ends[random.randint(0, len(female_surname_ends) - 1)]
        return surname

    def __generate_email(self, name, surname):
        domains = ['somemail.com', 'anothermail.net', 'imaginarymail.com']
        at = '@'
        dot = '.'
        ending = str(random.randint(1, 999))
        domain_name = random.choice(domains)

        mail = name + dot + surname + ending + at + domain_name
        valid_mail = re.sub(r'[^\x00-\x7F]+', '', mail)
        return valid_mail

    def __generate_phone(self):
        dialling_code = '048'
        digits = string.digits
        number_chars = random.choices(digits, k=9)

        number = ''
        for c in number_chars:
            number += c

        return dialling_code + number

    def __generate_password(self):
        length = random.randint(8, 16)
        chars = string.ascii_letters

        password_chars = random.choices(chars, k=length)

        password = ''
        for c in password_chars:
            password += c

        return password

    def __generate_pesel(self, date, sex):
        pesel_date = self.__create_pesel_date(date)
        series = self.__create_pesel_series(sex)
        checksum = self.__create_pesel_checksum(pesel_date + series)
        pesel = pesel_date + series + checksum
        while not self.__is_unique(pesel):
            series = self.__create_pesel_series(sex)
            checksum = self.__create_pesel_checksum(pesel_date + series)
            pesel = pesel_date + series + checksum
        return pesel

    def __create_pesel_date(self, date):
        pesel_date = ""
        if 1900 < date.year < 2000:
            year = str(date.year % 1900)
            pesel_date = self.__fix_length(year, 2)
            month = str(date.month)
            pesel_date += self.__fix_length(month, 2)
        elif 2000 <= date.year < 2099:
            year = str(date.year % 2000)
            year = self.__fix_length(year, 2)
            pesel_date = year
            month = 20 + date.month
            pesel_date += str(month)
        day = self.__fix_length(str(date.day), 2)
        pesel_date += day
        return pesel_date

    def __create_pesel_series(self, sex):
        series = random.randint(0, 9999)
        if sex == 1:
            while series % 2 != 1:
                series = random.randint(0, 9999)
        elif sex == 0:
            while series % 2 != 0:
                series = random.randint(0, 9999)
        return self.__fix_length(str(series), 4)

    def __create_pesel_checksum(self, pesel):
        checksum = (int(pesel[0]) * 1) % 10 + (int(pesel[1]) * 3) % 10 \
                   + (int(pesel[2]) * 7) % 10 + (int(pesel[3]) * 9) % 10
        checksum += (int(pesel[4]) * 1) % 10 + (int(pesel[5]) * 3) % 10 \
                    + (int(pesel[6]) * 7) % 10 + (int(pesel[7]) * 9) % 10 \
                    + (int(pesel[8]) * 1) % 10 + (int(pesel[9]) * 3) % 10
        return str((10 - checksum) % 10)

    def __fix_length(self, date, length):
        while len(date) < length:
            date = "0" + date
        return date

    def __is_unique(self, pesel):
        duplicate_list = list(Person.objects.filter(pesel=pesel).values())
        if len(duplicate_list) > 0:
            return False
        else:
            return True
