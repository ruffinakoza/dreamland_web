# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-28 23:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searcher', '0010_item_damage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='damage',
            field=models.CharField(default='', max_length=16),
        ),
    ]
