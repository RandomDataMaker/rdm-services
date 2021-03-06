# Generated by Django 3.0 on 2019-12-19 21:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('surname', models.CharField(max_length=30)),
                ('pesel', models.CharField(max_length=11)),
                ('sex', models.CharField(max_length=1)),
                ('birthday', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'db_table': 'peselgen_person',
            },
        ),
    ]
