# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-04 02:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landscape', '0004_auto_20161026_1936'),
    ]

    operations = [
        migrations.RenameField(
            model_name='landcover',
            old_name='shape',
            new_name='geometry',
        ),
    ]