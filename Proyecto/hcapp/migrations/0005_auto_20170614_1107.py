# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-14 16:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hcapp', '0004_auto_20170614_1030'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cerebrosimple',
            name='Estudio',
        ),
        migrations.AddField(
            model_name='pedido',
            name='CerebroSimple',
            field=models.ForeignKey(default='SOME STRING', on_delete=django.db.models.deletion.DO_NOTHING, to='hcapp.CerebroSimple'),
        ),
        migrations.DeleteModel(
            name='Estudio',
        ),
    ]
