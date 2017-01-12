# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-10 19:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20170110_1833'),
    ]

    operations = [
        migrations.AddField(
            model_name='quizset',
            name='Created_Date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='quizset',
            name='Published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
