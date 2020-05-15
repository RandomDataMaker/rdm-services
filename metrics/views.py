import multiprocessing

from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView

from metrics.metrics_service import MetricsService
from metrics.models import PatientMetrics


class MetricsView(APIView):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.metrics_service = MetricsService()

    def get(self, request):
        """
        Http get method to get all persons or person with given pesel
        Example url to get person by pesel: localhost:8000/person/12345678901
        :param request: has string parameter pesel
        :return: JSON response
        """

        metric_id = request.GET.get('id')
        patient_id = request.GET.get('patient_id')
        if metric_id:
            metric = list(PatientMetrics.objects.filter(id=metric_id).values())
            if len(metric) > 1:
                return HttpResponse(status=500)
            if not metric:
                return HttpResponse(status=404)
            else:
                return JsonResponse(metric[0], safe=False)
        if patient_id:
            patient_metrics = list(PatientMetrics.objects.filter(patient_id=patient_id).values())
            if not patient_metrics:
                return HttpResponse(status=404)
            else:
                return JsonResponse(patient_metrics, safe=False)

        metrics_list = list(PatientMetrics.objects.all().values())
        return JsonResponse(metrics_list, safe=False)

    def post(self, request, number=1):
        """
        Http method to generate persons and save them to database
        Example url to generate six persons: localhost:8000/person/6
        :param number: number of generated persons, default is 1
        :return: http status for created
        """
        for i in range(0, number):
            metrics = self.metrics_service.create_metrics()
            metrics.save()

        return HttpResponse(status=201)
