from rest_framework import serializers

from attributes.models import MetricsAttributes
from metrics.models import PatientMetrics
from person.models import Person


class AttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetricsAttributes
        fields = "__all__"