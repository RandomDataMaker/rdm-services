# Generated by Django 2.2.6 on 2019-10-20 21:09

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('person_service', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='birthday',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 20, 21, 9, 25, 917006, tzinfo=utc)),
        ),
    ]
