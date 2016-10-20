# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-28 14:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0012_question_cnt_list'),
    ]

    operations = [
        migrations.AddField(
            model_name='answeredquestion',
            name='game',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='questionnaire.Game'),
            preserve_default=False,
        ),
    ]