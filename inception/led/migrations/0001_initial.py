# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-04 03:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Led',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('led_wattage', models.CharField(choices=[('6', '6_watt'), ('9', '9_watt'), ('12', '12_watt')], max_length=3)),
            ],
        ),
    ]
