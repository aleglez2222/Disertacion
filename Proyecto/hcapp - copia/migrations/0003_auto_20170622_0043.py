# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-22 05:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hcapp', '0002_plantilla_nombredoc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plantilla',
            name='NombreDoc',
            field=models.CharField(max_length=200),
        ),
    ]
