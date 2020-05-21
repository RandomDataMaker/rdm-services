from rest_framework import serializers

from metrics.models import PatientMetrics
from person.models import Person


class MetricsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientMetrics
        fields = "__all__"