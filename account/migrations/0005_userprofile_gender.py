# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2020-01-24 05:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_remove_userprofile_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='gender',
            field=models.TextField(default='pria'),
            preserve_default=False,
        ),
    ]
