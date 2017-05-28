# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-27 02:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=2000)),
                ('quantity', models.IntegerField(default=0)),
                ('update_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Equipment',
                'verbose_name_plural': 'Equipments',
                'ordering': ('-update_date',),
            },
        ),
    ]