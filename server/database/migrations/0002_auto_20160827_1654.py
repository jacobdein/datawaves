# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-27 16:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sound_directory', models.CharField(max_length=1000)),
            ],
        ),
        migrations.RenameField(
            model_name='sound',
            old_name='filepath',
            new_name='custom_filepath',
        ),
    ]
