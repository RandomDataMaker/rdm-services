from drf_yasg import openapi
from rest_framework import status

from metrics.serializer import MetricsSerializer


class MetricSwagger:
    get_parameters = [
        openapi \
            .Parameter('id', in_=openapi.IN_QUERY,
                       description='Metric id', type=openapi.TYPE_INTEGER),
        openapi \
            .Parameter('patient_id', in_=openapi.IN_QUERY,
                       description='Get metrics of patient with given id', type=openapi.TYPE_INTEGER)
    ]

    get_responses = {
        status.HTTP_200_OK: openapi.Response('OK', MetricsSerializer),
        status.HTTP_404_NOT_FOUND: openapi.Response('NOT FOUND'),
        status.HTTP_500_INTERNAL_SERVER_ERROR: openapi.Response('INTERNAL SERVER ERROR')
    }

    post_parameters = [
        openapi \
                .Parameter('number', in_=openapi.IN_PATH, description='Number of generated persons',
                           type=openapi.TYPE_INTEGER, default=1)
    ]

    post_responses = {
        status.HTTP_201_CREATED: openapi.Response('CREATED', MetricsSerializer)
    }
