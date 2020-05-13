import jsonfield
from django.db import models


class MetricsAttributes(models.Model):
    person_id = models.CharField(max_length=30)
    geojson = jsonfield.JSONField()

    def __str__(self):
        return self.person_id + ' ' + self.geojson

    class Meta:
        db_table = "peselgen_geolocation"
