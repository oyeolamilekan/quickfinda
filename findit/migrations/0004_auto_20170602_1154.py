# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-02 18:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('findit', '0003_auto_20170602_0406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='analytics',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='findit.Products'),
        ),
    ]
