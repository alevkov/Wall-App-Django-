# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-15 19:19
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallapp', '0004_auto_20160515_1902'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='user',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='wallpost',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 15, 19, 19, 21, 994038)),
        ),
    ]
