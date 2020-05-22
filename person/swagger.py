from drf_yasg import openapi
from rest_framework import status

from person.serializer import PersonSerializer

class PersonSwagger:
    anonymize_list = ["id", "first_name", "last_name", "pesel", "password", "email", "phone", "sex", "birth_date"]
    get_parameters = [
        openapi \
            .Parameter('pesel', in_=openapi.IN_QUERY,
                       description='Pesel number - eleven numbers', type=openapi.TYPE_STRING),
        openapi \
            .Parameter('anonymize_array', in_=openapi.IN_QUERY,
                       description='Choose elements to hide from list:\n'
                                   'id, first_name, last_name, pesel, password, email, phone, sex, birth_date\n'
                                   'To get all public send: none',
                       type=openapi.TYPE_ARRAY, items=openapi.Items(type=openapi.TYPE_STRING),
                       default="first_name,last_name,pesel,password")
    ]

    get_responses = {
        status.HTTP_200_OK: openapi.Response('OK', PersonSerializer),
        status.HTTP_404_NOT_FOUND: openapi.Response('NOT FOUND'),
        status.HTTP_500_INTERNAL_SERVER_ERROR: openapi.Response('INTERNAL SERVER ERROR')
    }

    post_body = openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['number'],
            properties={
                'number': openapi.Schema(type=openapi.TYPE_INTEGER, default=1)
            },
        )

    post_responses = {
        status.HTTP_201_CREATED: openapi.Response('CREATED', PersonSerializer),
        status.HTTP_400_BAD_REQUEST: openapi.Response('BAD REQUEST')
    }

    delete_responses = {
        status.HTTP_201_CREATED: openapi.Response('CREATED', PersonSerializer),
        status.HTTP_500_INTERNAL_SERVER_ERROR: openapi.Response('INTERNAL SERVER ERROR'),
    }
