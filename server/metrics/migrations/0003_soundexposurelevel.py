# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-13 18:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0005_auto_20160912_1324'),
        ('metrics', '0002_auto_20160913_1819'),
    ]

    operations = [
        migrations.CreateModel(
            name='SoundExposureLevel',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('sel', models.CharField(max_length=500)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('analysis', models.ForeignKey(db_column='analysis', null=True, on_delete=django.db.models.deletion.SET_NULL, to='metrics.Analysis')),
                ('sound', models.ForeignKey(db_column='sound', on_delete=django.db.models.deletion.CASCADE, to='database.Sound')),
            ],
        ),
    ]
