from rest_framework import serializers

from geolocation.models import Geolocation


class GeolocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Geolocation
        fields = "__all__"
