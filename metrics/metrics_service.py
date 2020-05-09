from datetime import datetime
from random import randrange
from datetime import timedelta
import random
import logging

from attributes.attributes_service import AttributesService
from metrics.models import PatientMetrics
from person.models import Person


class MetricsService:

    def __init__(self):
        self.attributes_service = AttributesService('resources/attributes.model.json')

    def create_metrics(self):
        metrics = PatientMetrics()
        metrics.patient_id = self.__generate_patient_id()
        metrics.doctor_id = self.__generate_doctor_id()
        metrics.created = self.__generate_date()
        metrics.attributes_id = self.__generate_attributes()
        metrics.notes = self.__generate_notes()
        logging.basicConfig(level=logging.DEBUG)
        logging.info(f"Created metrics {metrics.patient_id} {metrics.doctor_id} with creation date {metrics.created}")
        return metrics

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
        date_now = datetime.now()
        date_first = datetime.now() + timedelta(days=-1000)

        date = self.__random_date(date_first, date_now)
        return date

    def __generate_patient_id(self):
        patients_id_list = Person.objects.filter().values_list('id', flat=True)
        patient_id = random.choice(patients_id_list)

        return str(patient_id)

    def __generate_doctor_id(self):
        return 'doctor_id'

    def __generate_notes(self):
        return 'some_notes'

    def __generate_attributes(self):
        attributes = self.attributes_service.generate_attributes()
        attributes.save()
        return attributes.id
