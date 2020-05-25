from django.http import HttpResponse, JsonResponse
from drf_yasg.utils import swagger_auto_schema
from rest_framework.utils import json
from rest_framework.views import APIView

from attributes.models import MetricsAttributes
from generator.swagger import GeneratorSwagger
from geolocation.geolocation_service import GeolocationService
from geolocation.models import Geolocation
from metrics.metrics_service import MetricsService
from metrics.models import PatientMetrics
from person.models import Person
from person.person_service import PersonService


class GeneratorView(APIView):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.person_service = PersonService('resources/person.model.json')
        self.metrics_service = MetricsService()
        self.geolocation_service = GeolocationService()

    @swagger_auto_schema(
        request_body=GeneratorSwagger.post_body,
        responses=GeneratorSwagger.post_responses,
        operation_id='Generate all',
        operation_description='This endpoint generates all data',
        operation_summary="Generate all data"
    )
    def post(self, request):
        number = 1
        if request.body:
            parsed_body = (json.loads(request.body))
            number = parsed_body.get("number")
            if number is None:
                return HttpResponse(status=400)
        for i in range(0, number):
            # creating new object
            person = self.person_service.create_person()
            person.save()

        for i in range(0, number):
            # creating new object
            metrics = self.metrics_service.create_metrics()
            metrics.save()

        country_polygon = self.geolocation_service.generate_country_polygon('POL')
        for i in range(0, number):
            # creating new object
            geolocation = self.geolocation_service.create_geolocation(country_polygon, 1, 'POL')
            geolocation.save()
        return HttpResponse(status=201)

    @swagger_auto_schema(
        responses=GeneratorSwagger.delete_responses,
        operation_id='Flush tables',
        operation_description='This endpoint flushes all tables',
        operation_summary="Flush all tables"
    )
    def delete(self, request):
        Geolocation.objects.all().delete()
        MetricsAttributes.objects.all().delete()
        PatientMetrics.objects.all().delete()
        Person.objects.all().delete()
        return HttpResponse(status=200)
