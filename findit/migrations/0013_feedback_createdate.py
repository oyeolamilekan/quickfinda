# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-15 22:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('findit', '0012_auto_20170612_1230'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='createdate',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
