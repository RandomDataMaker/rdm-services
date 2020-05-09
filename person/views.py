from django.http import HttpResponse, JsonResponse
from django.views import View
from person.models import Person
from person.person_service import PersonService


class PersonView(View):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.person_service = PersonService('resources/person.model.json')

    def get(self, request):
        """
        Http get method to get all persons or person with given pesel
        and anonymized according to anonymize array (e.g. email,pesel or none )
        Example url to get person by pesel: localhost:8000/person/?pesel=12345678901
        :param pesel: if provided finds only person with this pesel
        :param anonymize_array: array of attributes to anonymize, default - all
        :return: JSON response
        """
        pesel = request.GET.get('pesel')
        anonymize_array = request.GET.get('anonymize_array')
        if anonymize_array is None or anonymize_array == "":
            anonymize_array = "first_name,last_name,pesel,email,phone,sex,birth_date"
        if pesel:
            person = list(Person.objects.filter(pesel=pesel).values())
            if len(person) > 1:
                return HttpResponse(status=500)
            if not person:
                return HttpResponse(status=404)
            else:
                person = self.person_service.anonymize(person, anonymize_array)
                return JsonResponse(person[0], safe=False)
        else:
            person_list = list(Person.objects.all().values())
            for person in person_list:
                self.person_service.anonymize(person, anonymize_array)
            return JsonResponse(person_list, safe=False)

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
        return HttpResponse(status=201)
