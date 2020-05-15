from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from django.views import View
from geolocation.geolocation_service import Geolocationservice
from geolocation.models import  MetricsAttributes

# Create your views here.
class GeolocationView(View):

    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.geolocation_service=MetricsAttributes()


def get(self, request):
    """
    Http get method to get all persons or person with given pesel
    Example url to get person by pesel: localhost:8000/person/12345678901
    :param request: has string parameter pesel
    :return: JSON response
    """
    person_id=request.GET.get('id')
    if person_id:
        person=list(Geolocationservice.object.filter(id=person_id).values())
        if not person:
            return HttpResponse(status=404)
        else:
            return JsonResponse(person,safe=False)
    person_list=list(Geolocationservice.object.all().values())
    return JsonResponse(person_list,safe=False)

def post(self, request, number=1):
        """
        Http method to generate persons and save them to database
        Example url to generate six persons: localhost:8000/person/6
        :param number: number of generated persons, default is 1
        :return: http status for created
        """
        for i in range(0,number):
            location=self.geolocation_service.create_geolocation()
            location.save()

        return HttpResponse(status=201)