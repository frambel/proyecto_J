# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2020-01-05 20:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dstore', '0005_artista_artista'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artista',
            name='artista',
            field=models.ImageField(blank=True, null=True, upload_to='foto_artista'),
        ),
        migrations.AlterField(
            model_name='disquera',
            name='domicilio',
            field=models.CharField(blank=True, max_length=90),
        ),
    ]
