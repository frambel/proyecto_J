# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2020-01-06 18:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dstore', '0008_auto_20200105_1909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artista',
            name='apellido',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='artista',
            name='nombre',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
