# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2020-01-22 12:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='phone',
            field=models.IntegerField(blank=True, default=62, null=True),
        ),
    ]