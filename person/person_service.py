import re
import string
from datetime import datetime
from random import randrange
from datetime import timedelta
import random
import logging
import hashlib

from person.models import Person


class PersonService:

    def create_person(self):
        person = Person()
        person.sex = self.__generate_sex()
        person.birth_date = self.__generate_date()
        person.first_name = self.__generate_name(person.sex)
        person.last_name = self.__generate_surname(person.sex)
        person.pesel = self.__generate_pesel(person.birth_date, person.sex)
        person.email = self.__generate_email(person.first_name, person.last_name)
        person.phone = self.__generate_phone()
        person.password = self.__generate_password()
        logging.basicConfig(level=logging.DEBUG)
        logging.info(f"Created person {person.first_name} {person.last_name} with pesel {person.pesel}")
        return person

    def anonymize(self, person, anonymize_array):
        person["hash"] = ""
        person["password"] = ""
        anonymize_array = anonymize_array.split(',')
        if anonymize_array[0] == 'none':
            return person

        for item in anonymize_array:
            person["hash"] += str(person[item])
            person[item] = ""

        person["hash"] = hashlib.sha3_256(person["hash"].encode('utf-8')).hexdigest()
        return person

    def __random_date(self, start, end):
        """
        This function will return a random datetime between two datetime
        objects.
        """
        delta = end - start
        int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
        random_second = randrange(int_delta)
        return start + timedelta(seconds=random_second)

    def __generate_date(self):
        rand = random.randint(0, 3655)
        d1 = datetime.strptime('1/1/1970 1:30 PM', '%m/%d/%Y %I:%M %p')
        d2 = datetime.strptime('12/31/1975 4:50 AM', '%m/%d/%Y %I:%M %p')
        # TODO Mozna dodawac wiecej lat
        if (0 < rand < 580):
            # YEARS 1970-1976
            d1 = datetime.strptime('1/1/1970 1:30 PM', '%m/%d/%Y %I:%M %p')
            d2 = datetime.strptime('12/31/1975 4:50 AM', '%m/%d/%Y %I:%M %p')
        if (580 < rand < 1280):
            d1 = datetime.strptime('1/1/1976 1:30 PM', '%m/%d/%Y %I:%M %p')
            d2 = datetime.strptime('12/31/1981 4:50 AM', '%m/%d/%Y %I:%M %p')
            # YEARS 1976-1982
        if (1280 < rand < 1930):
            d1 = datetime.strptime('1/1/1982 1:30 PM', '%m/%d/%Y %I:%M %p')
            d2 = datetime.strptime('12/31/1987 4:50 AM', '%m/%d/%Y %I:%M %p')
            # YEARS 1982-1988
        if (1930 < rand < 2480):
            d1 = datetime.strptime('1/1/1988 1:30 PM', '%m/%d/%Y %I:%M %p')
            d2 = datetime.strptime('12/31/1993 4:50 AM', '%m/%d/%Y %I:%M %p')
            # YEARS 1988-1994
        if (2480 < rand < 2880):
            d1 = datetime.strptime('1/1/1994 1:30 PM', '%m/%d/%Y %I:%M %p')
            d2 = datetime.strptime('12/31/1999 4:50 AM', '%m/%d/%Y %I:%M %p')
            # YEARS 1994-2000
        if (2880 < rand < 3255):
            d1 = datetime.strptime('1/1/2000 1:30 PM', '%m/%d/%Y %I:%M %p')
            d2 = datetime.strptime('12/31/2005 4:50 AM', '%m/%d/%Y %I:%M %p')
            # YEARS 2000-2006
        if (3255 < rand < 3655):
            d1 = datetime.strptime('1/1/2006 1:30 PM', '%m/%d/%Y %I:%M %p')
            d2 = datetime.strptime('12/31/2013 4:50 AM', '%m/%d/%Y %I:%M %p')
            # YEARS 2006-2014

        date = self.__random_date(d1, d2)
        return date

    def __generate_sex(self):
        rand = random.randint(0, 206)
        while 1:
            if rand < 100:
                return 1
            else:
                return 0

    def __generate_name(self, sex):
        names = []
        # loading the names from .txt depending from sex
        if sex == 1:
            names = [line.rstrip('\n') for line in open('./person/mens_name.txt', encoding="utf8")]
        else:
            names = [line.rstrip('\n') for line in open('./person/girls_name.txt', encoding="utf8")]
        rand = random.randint(0, len(names) - 1)
        return names[rand]

    def __generate_surname(self, sex):
        # creating variable
        vowel = ["a", "e", "i", "o", "u", "y"]
        consonants = ["b", "c", "d", "g", "h", "j", "k", "l", "m", "n", "p", "r", "s", "t", "w", "z"]
        male_surname_ends = ["ski", "cki", "dzki", "ak", "ek", "ik", "yk", "ki", "owicz", "eowicz", "ewicz", "el", "ny",
                             "uk", "in", "ny"]
        female_surname_ends = ["ska", "cka", "dzka", "ak", "ek", "ik", "yk", "ka", "owicz", "eowicz", "na", "ul", "uk"]
        surname = ""
        # generating the first 3 letters of surname
        surname = consonants[random.randint(0, len(consonants) - 1)].upper() \
                  + vowel[random.randint(0, len(vowel) - 1)] \
                  + consonants[random.randint(0, len(consonants) - 1)]
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
