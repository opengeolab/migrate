# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-16 15:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0003_auto_20160916_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='data_source_link',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='question',
            name='license_link',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]
