# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-28 02:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searcher', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='level',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
