# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-09 15:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('findit', '0010_auto_20170607_2321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
    ]
