# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-15 20:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0005_auto_20160912_1324'),
        ('metrics', '0005_auto_20160913_1937'),
    ]

    operations = [
        migrations.CreateModel(
            name='AcousticComplexityIndex',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('aci_left', models.FloatField()),
                ('aci_right', models.FloatField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('analysis', models.ForeignKey(db_column='analysis', null=True, on_delete=django.db.models.deletion.SET_NULL, to='metrics.Analysis')),
                ('sound', models.ForeignKey(db_column='sound', on_delete=django.db.models.deletion.CASCADE, to='database.Sound')),
            ],
            options={
                'verbose_name_plural': 'acoustic complexity indices',
            },
        ),
    ]