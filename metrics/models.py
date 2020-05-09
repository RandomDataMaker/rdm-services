from datetime import datetime

from django.db import models


# Create your models here.
class PatientMetrics(models.Model):
    patient_id = models.CharField(max_length=30)
    doctor_id = models.CharField(max_length=30)
    created = models.DateTimeField(default=datetime.now)
    attributes_id = models.CharField(max_length=30)
    notes = models.CharField(max_length=1024)

    def __str__(self):
        return str(self.patient_id) + " " + self.doctor_id + " " + str(self.created) + " " + self.notes

    class Meta:
        db_table = "peselgen_metrics"
