from django.http import JsonResponse, HttpResponse
from rest_framework.utils import json
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
        operation_summary="Get all attributes or find by id"
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
        request_body=AttributeSwagger.post_body,
        responses=AttributeSwagger.post_responses,
        operation_id='Generate attributes',
        operation_description='This endpoint generates attribute or number of attributes',
        operation_summary="Generate attribute with random data"
    )
    def post(self, request):
        number = 1
        if request.body:
            parsed_body = (json.loads(request.body))
            number = parsed_body.get("number")
            if number is None:
                return HttpResponse(status=400)
        for i in range(0, number):
            attributes = self.attributes_service.generate_attributes()
            attributes.save()

        return HttpResponse(status=201)

    @swagger_auto_schema(
        responses=AttributeSwagger.delete_responses,
        operation_id='Flush attributes',
        operation_description='This endpoint flushes attribute\'s table',
        operation_summary="Flush table of attributes"
    )
    def delete(self, request):
        MetricsAttributes.objects.all().delete()
        return HttpResponse(status=200)