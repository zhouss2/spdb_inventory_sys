# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-06 13:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipments', '0005_auto_20170804_1659'),
    ]

    operations = [
        migrations.AddField(
            model_name='operation',
            name='remark',
            field=models.TextField(blank=True, max_length=2000, null=True),
        ),
    ]
