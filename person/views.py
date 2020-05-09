from django.http import HttpResponse, JsonResponse
from django.views import View
from person.models import Person
from datetime import datetime
from random import randrange
from datetime import timedelta
import random

from person.person_service import PersonService


class PersonView(View):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.person_service = PersonService('resources/person.model.json')

    def get(self, request):
        """
        Http get method to get all persons or person with given pesel
        Example url to get person by pesel: localhost:8000/person/12345678901
        :param request: has string parameter pesel
        :return: JSON response
        """
        pesel = request.GET.get('pesel')
        if pesel:
            person = list(Person.objects.filter(pesel=pesel).values())[0]
        else:
            person_list = list(Person.objects.all().values())
            return JsonResponse(person_list, safe=False)

    def post(self, request, number=1):
        """
        Http method to generate persons and save them to database
        Example url to generate six persons: localhost:8000/person/6
        :param number: number of generated persons, default is 1
        :return: http status for created
        """
        for i in range(0, number):
            # creating new object
            person = self.person_service.create_person()
            person.save()
        return HttpResponse(status=201)
