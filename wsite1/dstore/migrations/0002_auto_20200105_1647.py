# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2020-01-05 19:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dstore', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('instagram', models.CharField(blank=True, max_length=30)),
                ('twitter', models.CharField(blank=True, max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='disquera',
            name='sitioweb',
            field=models.URLField(blank=True),
        ),
    ]
