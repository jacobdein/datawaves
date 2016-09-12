# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-12 13:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0004_auto_20160827_1932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sound',
            name='quality',
            field=models.IntegerField(blank=True, choices=[(0, 'none'), (1, 'one'), (2, 'two'), (3, 'three')], default=0),
        ),
    ]
