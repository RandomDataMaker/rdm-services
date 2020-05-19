from django.contrib import admin

# Register your models here.
from attributes.models import MetricsAttributes
from metrics.models import PatientMetrics
from person.models import Person

admin.site.register(Person)
admin.site.register(MetricsAttributes)
admin.site.register(PatientMetrics)