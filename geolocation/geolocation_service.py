from django.db import models
import pycristoforo as pyc
from person.models import Person
from geolocation.models import Geolocation
import random
import logging


class GeolocationService:
    def create_geolocation(self):
        location = Geolocation()
        location.geojson = self.__generate_geolocation()
        location.person_id = self.__generate_person_id()
        logging.basicConfig(level=logging.DEBUG)
        logging.info(
            f"Created metrics {location.person_id} with created location {location.geojson[0]['geometry']['coordinates']}")
        return location

    def __generate_geolocation(self):
        country = pyc.get_shape("POL")
        points = pyc.geoloc_generation(country, 1, "POL")
        pyc.geoloc_print(points, ',')

        return points

    def __generate_person_id(self):
        person_id_list = Person.objects.filter().values_list('id', flat=True)
        person_id = random.choice(person_id_list)

        return str(person_id)
