# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2020-01-05 20:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dstore', '0003_auto_20200105_1700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artista',
            name='artistico',
            field=models.CharField(max_length=30),
        ),
    ]
