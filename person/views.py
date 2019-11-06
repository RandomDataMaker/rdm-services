from django.http import HttpResponse, JsonResponse

# Create your views here.
from django.views import View
from rest_framework.utils import json

from person.models import Person


class PersonView(View):

    def get(self, request):
        """
        Http get method to get all persons or person with given pesel
        Example url to get person by pesel: localhost:8000/person/12345678901
        :param request: has string parameter pesel
        :return: JSON response
        """
        pesel = request.GET.get('pesel')
        if pesel:
            person = list(Person.objects.filter(pesel=pesel).values())[0] #TODO exception if more than one
            return JsonResponse(person, safe=False)
        else:
            person_list = list(Person.objects.all().values())
            return JsonResponse(person_list, safe=False)

    def post(self, request, number=1):
        for i in range(0, number):
            # TODO: put here code for generate
            pass
        return HttpResponse(status=201)

