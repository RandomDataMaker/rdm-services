from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView

from metrics.metrics_service import MetricsService
from metrics.models import PatientMetrics
from drf_yasg.utils import swagger_auto_schema

from metrics.swagger import MetricSwagger


class MetricsView(APIView):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.metrics_service = MetricsService()

    @swagger_auto_schema(
        manual_parameters=MetricSwagger.get_parameters,
        responses=MetricSwagger.get_responses,
        operation_id='List of metrics',
        operation_description='This endpoint returns list of metrics or specified metric or metrics for one patient',
    )
    def get(self, request):
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

    @swagger_auto_schema(
        manual_parameters=MetricSwagger.post_parameters,
        responses=MetricSwagger.post_responses,
        operation_id='Generate metrics',
        operation_description='This endpoint generates random metrics',
    )
    def post(self, request, number=1):
        for i in range(0, number):
            metrics = self.metrics_service.create_metrics()
            metrics.save()

        return HttpResponse(status=201)
