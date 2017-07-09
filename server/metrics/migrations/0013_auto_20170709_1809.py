# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-07-09 18:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metrics', '0012_soundscaperatio_biophony_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='soundexposurelevel',
            name='anthrophony',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='soundexposurelevel',
            name='biophony',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='soundexposurelevel',
            name='sel_bins',
            field=models.CharField(max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='soundexposurelevel',
            name='sel',
            field=models.FloatField(null=True),
        ),
    ]
