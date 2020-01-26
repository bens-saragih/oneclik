# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2020-01-24 12:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_remove_userprofile_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(choices=[('Pria', 'Pria'), ('Wanita', 'Wanita')], default='pria', max_length=20),
            preserve_default=False,
        ),
    ]
