from django.http import JsonResponse, HttpResponse
from django.views import View

from attributes.attributes_service import AttributesService
from attributes.models import MetricsAttributes


class AttributesView(View):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.attributes_service = AttributesService('resources/attributes.model.json')

    def get(self, request):
        """
        Http get method to get all persons or person with given pesel
        Example url to get person by pesel: localhost:8000/person/12345678901
        :param request: has string parameter pesel
        :return: JSON response
        """
        attr_id = request.GET.get('id')
        if attr_id:
            attr = list(MetricsAttributes.objects.filter(id=attr_id).values())
            if len(attr) > 1:
                return HttpResponse(status=500)
            if not attr:
                return HttpResponse(status=404)
            else:
                return JsonResponse(attr[0], safe=False)
        else:
            attributes_list = list(MetricsAttributes.objects.all().values())
            return JsonResponse(attributes_list, safe=False)

    def post(self, request, number=1):
        """
        Http method to generate persons and save them to database
        Example url to generate six persons: localhost:8000/person/6
        :param number: number of generated persons, default is 1
        :return: http status for created
        """
        for i in range(0, number):
            attributes = self.attributes_service.generate_attributes()
            attributes.save()

        return HttpResponse(status=201)
