# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-27 15:34
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0007_auto_20161026_1653'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='shape',
            field=django.contrib.gis.db.models.fields.PointField(null=True, srid=31254),
        ),
    ]
