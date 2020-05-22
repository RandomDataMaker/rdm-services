from drf_yasg import openapi
from rest_framework import status

from attributes.serializer import AttributeSerializer


class AttributeSwagger:
    get_parameters = [
        openapi \
            .Parameter('id', in_=openapi.IN_QUERY,
                       description='Attribute id', type=openapi.TYPE_INTEGER),
    ]

    get_responses = {
        status.HTTP_200_OK: openapi.Response('OK', AttributeSerializer),
        status.HTTP_404_NOT_FOUND: openapi.Response('NOT FOUND'),
        status.HTTP_500_INTERNAL_SERVER_ERROR: openapi.Response('INTERNAL SERVER ERROR')
    }

    post_body = openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['number'],
            properties={
                'number': openapi.Schema(type=openapi.TYPE_INTEGER, default=1, example=1)
            },
        )

    post_responses = {
        status.HTTP_201_CREATED: openapi.Response('CREATED', AttributeSerializer),
        status.HTTP_400_BAD_REQUEST: openapi.Response('BAD REQUEST')
    }

    delete_responses = {
        status.HTTP_201_CREATED: openapi.Response('CREATED', AttributeSerializer),
        status.HTTP_500_INTERNAL_SERVER_ERROR: openapi.Response('INTERNAL SERVER ERROR'),
    }
