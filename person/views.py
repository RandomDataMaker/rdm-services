from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from person.models import Person
from person.person_service import PersonService
from anonymization.anonymize import anonymize
from person.serializer import PersonSerializer
from person.swagger_variables import get_parameters, get_responses, post_responses, post_parameters


class PersonView(APIView):  # GenericAPIView
    """
        Person documentation
    """

    serializer_class = PersonSerializer
    model = Person
    queryset = Person.objects.all()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.person_service = PersonService('resources/person.model.json')

    @swagger_auto_schema(
        manual_parameters=get_parameters,
        responses=get_responses,
        operation_id='List of persons',
        operation_description='This endpoint returns list of persons in database or specified person',
    )
    def get(self, request):
        pesel = request.GET.get('pesel')
        anonymize_array = request.GET.get('anonymize_array')
        if anonymize_array is None or anonymize_array == "":
            anonymize_array = "id,first_name,last_name,pesel,password,email,phone,sex,birth_date"
        if pesel:
            person = list(Person.objects.filter(pesel=pesel).values())
            if len(person) > 1:
                return HttpResponse(status=500)
            if not person:
                return HttpResponse(status=404)
            else:
                person = anonymize(person[0], anonymize_array)
                return JsonResponse(person, safe=False)
        else:
            person_list = [anonymize(person, anonymize_array) for person in list(Person.objects.all().values())]
            return JsonResponse(person_list, safe=False)

    @swagger_auto_schema(
        responses=post_responses,
        operation_id='Generate person',
        operation_description='This endpoint generates person with random personal data',
    )
    def post(self, request):
        person = self.person_service.create_person()
        person.save()
        return HttpResponse(status=201)


class PersonCreateView(APIView):
    serializer_class = PersonSerializer
    model = Person
    queryset = Person.objects.all()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.person_service = PersonService('resources/person.model.json')

    @swagger_auto_schema(
        manual_parameters=post_parameters,
        responses=post_responses,
        operation_id='Generate number of persons',
        operation_description='This endpoint generates persons with random personal data',
    )
    def post(self, request, number=1):
        for i in range(0, number):
            person = self.person_service.create_person()
            person.save()
        return HttpResponse(status=201)