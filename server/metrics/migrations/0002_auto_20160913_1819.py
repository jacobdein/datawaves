# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-13 18:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('metrics', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Call',
            new_name='Analysis',
        ),
        migrations.RemoveField(
            model_name='soundscapespec',
            name='call',
        ),
        migrations.AddField(
            model_name='soundscapespec',
            name='analysis',
            field=models.ForeignKey(db_column='analysis', null=True, on_delete=django.db.models.deletion.SET_NULL, to='metrics.Analysis'),
        ),
    ]
