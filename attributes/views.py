from django.http import JsonResponse, HttpResponse
from rest_framework.views import APIView

from attributes.attributes_service import AttributesService
from attributes.models import MetricsAttributes
from drf_yasg.utils import swagger_auto_schema
from attributes.swagger import AttributeSwagger


class AttributesView(APIView):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.attributes_service = AttributesService('resources/attributes.model.json')

    @swagger_auto_schema(
        manual_parameters=AttributeSwagger.get_parameters,
        responses=AttributeSwagger.get_responses,
        operation_id='List of attributes',
        operation_description='This endpoint returns list of attributes in database or specified attribute',
    )
    def get(self, request):
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

    @swagger_auto_schema(
        manual_parameters=AttributeSwagger.post_parameters,
        responses=AttributeSwagger.post_responses,
        operation_id='List of attributes',
        operation_description='This endpoint returns list of attributes in database or specified attribute',
    )
    def post(self, request, number=1):
        for i in range(0, number):
            attributes = self.attributes_service.generate_attributes()
            attributes.save()

        return HttpResponse(status=201)
