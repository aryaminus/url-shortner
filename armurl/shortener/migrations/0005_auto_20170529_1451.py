# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-29 14:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0004_auto_20170527_0822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='armurl',
            name='shortcode',
            field=models.CharField(blank=True, max_length=15, unique=True),
        ),
    ]
