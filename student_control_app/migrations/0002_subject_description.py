# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-12-05 21:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_control_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
