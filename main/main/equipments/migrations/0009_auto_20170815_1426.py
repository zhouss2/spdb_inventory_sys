# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-15 06:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('equipments', '0008_equipmentareaidle'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipmentareaidle',
            name='equipment_area',
        ),
        migrations.AddField(
            model_name='equipmentareaidle',
            name='area',
            field=models.ForeignKey(default=5, on_delete=django.db.models.deletion.CASCADE, to='equipments.Area'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='equipmentareaidle',
            name='equipment',
            field=models.ForeignKey(default=70, on_delete=django.db.models.deletion.CASCADE, to='equipments.Equipment'),
            preserve_default=False,
        ),
    ]
