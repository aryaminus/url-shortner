# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-22 12:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='armurl',
            name='shortcode',
            field=models.CharField(default='shortcode', max_length=15),
            preserve_default=False,
        ),
    ]