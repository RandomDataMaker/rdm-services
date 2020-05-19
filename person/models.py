from datetime import datetime

from django.db import models


# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    pesel = models.CharField(max_length=11)
    email = models.CharField(max_length=64)
    phone = models.CharField(max_length=12)
    password = models.CharField(max_length=64)
    # true means that person is a male
    sex = models.CharField(max_length=1)
    birth_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.first_name + " " + self.last_name + " " + self.pesel

    class Meta:
        db_table = "peselgen_person"
