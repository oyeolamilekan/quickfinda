# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-10-17 22:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adengine', '0010_ads_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ads',
            name='ad_type',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
    ]
