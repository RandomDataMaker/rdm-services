from django.http import HttpResponse, JsonResponse
from django.views import View

from attributes.models import MetricsAttributes
from metrics.metrics_service import MetricsService
from metrics.models import PatientMetrics
from person.models import Person
from person.person_service import PersonService


class GeneratorView(View):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.person_service = PersonService('resources/person.model.json')
        self.metrics_service = MetricsService()

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

        for i in range(0, number):
            # creating new object
            metrics = self.metrics_service.create_metrics()
            metrics.save()
        return HttpResponse(status=201)

    def put(self, request, table=''):
        """
        Http method to generate persons and save them to database
        Example url to generate six persons: localhost:8000/person/6
        :param number: number of generated persons, default is 1
        :return: http status for created
        """
        if table == 'attributes':
            MetricsAttributes.objects.all().delete()

        elif table == 'metrics':
            PatientMetrics.objects.all().delete()

        elif table == 'person':
            Person.objects.all().delete()

        elif table == '':
            MetricsAttributes.objects.all().delete()
            PatientMetrics.objects.all().delete()
            Person.objects.all().delete()

        else:
            return HttpResponse(status=422)

        return HttpResponse(status=200)
