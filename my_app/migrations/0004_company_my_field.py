# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-11-07 00:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('My application', '0003_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='my_field',
            field=models.BooleanField(default=True),
        ),
    ]
