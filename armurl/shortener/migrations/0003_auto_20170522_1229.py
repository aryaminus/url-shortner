# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-22 12:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0002_armurl_shortcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='armurl',
            name='shortcode',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]