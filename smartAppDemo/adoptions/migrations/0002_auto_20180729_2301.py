# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-29 23:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adoptions', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pet',
            name='vaccination',
        ),
        migrations.AddField(
            model_name='pet',
            name='vaccinations',
            field=models.ManyToManyField(blank=True, to='adoptions.Vaccine'),
        ),
    ]
