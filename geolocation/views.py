from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from django.views import View
from drf_yasg.utils import swagger_auto_schema
from rest_framework.utils import json
from rest_framework.views import APIView

from geolocation.geolocation_service import GeolocationService
from geolocation.models import Geolocation


# Create your views here.
from geolocation.serializer import GeolocationSerializer
from geolocation.swagger import GeolocationSwagger


class GeolocationView(APIView):

    serializer_class = GeolocationSerializer
    model = Geolocation
    queryset = Geolocation.objects.all()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.geolocation_service = GeolocationService()

    @swagger_auto_schema(
        manual_parameters=GeolocationSwagger.get_parameters,
        responses=GeolocationSwagger.get_responses,
        operation_id='List of geolocation points',
        operation_description='This endpoint returns list of geolocation objects or specified geolocation or '
                              'geolocation for one patient',
        operation_summary="Get all geolocation or find by id or person id"
    )
    def get(self, request):
        person_id = request.GET.get('id')
        if person_id:
            person = list(Geolocation.objects.filter(id=person_id).values())
            if not person:
                return HttpResponse(status=404)
            else:
                return JsonResponse(person, safe=False)
        person_list = list(Geolocation.objects.all().values())
        return JsonResponse(person_list, safe=False)

    @swagger_auto_schema(
        request_body=GeolocationSwagger.post_body,
        responses=GeolocationSwagger.post_responses,
        operation_id='Generate geolocation objects',
        operation_description='This endpoint generates random geolocation object or number of geolocation objects',
        operation_summary="Generate geolocation with random data"
    )
    def post(self, request):
        number = 1
        country = 'POL'
        points_number = 1
        properties = country
        if request.body:
            parsed_body = (json.loads(request.body))
            number = parsed_body.get("number")
            country = parsed_body.get("country")
            points_number = parsed_body.get("points_number")
            if number is None:
                return HttpResponse(status=400)
            if country is None:
                return HttpResponse(status=400)
            if points_number is None:
                return HttpResponse(status=400)
        for i in range(0, number):
            location = self.geolocation_service.create_geolocation(country, points_number, properties)
            location.save()

        return HttpResponse(status=201)

    @swagger_auto_schema(
        responses=GeolocationSwagger.delete_responses,
        operation_id='Flush geolocation',
        operation_description='This endpoint flushes geolocation\'s table',
        operation_summary="Flush table of geolocation"
    )
    def delete(self, request):
        Geolocation.objects.all().delete()
        return HttpResponse(status=200)
