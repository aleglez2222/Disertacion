# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-07 04:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hcapp', '0003_auto_20170622_0043'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='Historia',
        ),
        migrations.AddField(
            model_name='historia',
            name='Pedido',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='hcapp.Pedido'),
        ),
    ]
