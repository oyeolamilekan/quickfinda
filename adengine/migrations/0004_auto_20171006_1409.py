# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-10-06 14:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adengine', '0003_auto_20171005_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='click',
            name='date_added',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='view',
            name='date_added',
            field=models.DateTimeField(),
        ),
    ]
