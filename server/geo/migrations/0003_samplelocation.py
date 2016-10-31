# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-31 19:36
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geo', '0002_auto_20161027_1915'),
    ]

    operations = [
        migrations.CreateModel(
            name='SampleLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('probability', models.FloatField(blank=True)),
                ('landcover', models.FloatField(blank=True)),
                ('naturalness', models.IntegerField(blank=True)),
                ('shape', django.contrib.gis.db.models.fields.PolygonField(srid=31254)),
            ],
        ),
    ]
