# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-10-17 11:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adengine', '0008_ads_expired'),
    ]

    operations = [
        migrations.AddField(
            model_name='ads',
            name='ad_type',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]