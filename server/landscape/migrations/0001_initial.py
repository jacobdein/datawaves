# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-14 00:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('database', '0005_auto_20160912_1324'),
    ]

    operations = [
        migrations.CreateModel(
            name='LandCoverArea',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('included_area', models.CharField(max_length=50)),
                ('type_1', models.FloatField(blank=True)),
                ('type_2', models.FloatField(blank=True)),
                ('type_3', models.FloatField(blank=True)),
                ('type_4', models.FloatField(blank=True)),
                ('type_5', models.FloatField(blank=True)),
                ('type_6', models.FloatField(blank=True)),
                ('type_7', models.FloatField(blank=True)),
                ('type_8', models.FloatField(blank=True)),
                ('type_9', models.FloatField(blank=True)),
                ('type_10', models.FloatField(blank=True)),
                ('type_11', models.FloatField(blank=True)),
                ('type_12', models.FloatField(blank=True)),
                ('type_13', models.FloatField(blank=True)),
                ('type_14', models.FloatField(blank=True)),
                ('type_15', models.FloatField(blank=True)),
                ('site', models.ForeignKey(db_column='site', on_delete=django.db.models.deletion.CASCADE, to='database.Site')),
            ],
        ),
    ]
