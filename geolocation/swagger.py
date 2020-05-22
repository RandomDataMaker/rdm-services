from drf_yasg import openapi
from rest_framework import status

from metrics.serializer import MetricsSerializer


class GeolocationSwagger:
    get_parameters = [
        openapi \
            .Parameter('id', in_=openapi.IN_QUERY,
                       description='Geolocation id', type=openapi.TYPE_INTEGER),
        openapi \
            .Parameter('person_id', in_=openapi.IN_QUERY,
                       description='Get geolocation of person with given id', type=openapi.TYPE_INTEGER)
    ]

    get_responses = {
        status.HTTP_200_OK: openapi.Response('OK', MetricsSerializer),
        status.HTTP_404_NOT_FOUND: openapi.Response('NOT FOUND'),
        status.HTTP_500_INTERNAL_SERVER_ERROR: openapi.Response('INTERNAL SERVER ERROR')
    }

    post_body = openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=['number'],
        properties={
            'number': openapi.Schema(type=openapi.TYPE_INTEGER, default=1, example=1),
            'country': openapi.Schema(type=openapi.TYPE_STRING, default='POL', example='POL'),
            'points_number': openapi.Schema(type=openapi.TYPE_INTEGER, default=1, example=1)
        },
    )

    post_responses = {
        status.HTTP_201_CREATED: openapi.Response('CREATED', MetricsSerializer),
        status.HTTP_400_BAD_REQUEST: openapi.Response('BAD REQUEST')
    }

    delete_responses = {
        status.HTTP_201_CREATED: openapi.Response('CREATED', MetricsSerializer),
    }
