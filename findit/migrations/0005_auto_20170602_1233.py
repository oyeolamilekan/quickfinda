# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-02 19:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('findit', '0004_auto_20170602_1154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='analytics',
            name='product',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='findit.Products'),
        ),
    ]