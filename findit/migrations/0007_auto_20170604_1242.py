# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-04 19:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('findit', '0006_auto_20170602_1322'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='image',
            new_name='images',
        ),
    ]
