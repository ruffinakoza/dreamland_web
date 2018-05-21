# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-28 04:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searcher', '0003_item_wearloc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='wearloc',
            field=models.CharField(choices=[('none', 'none'), ('finger', 'finger'), ('neck', 'neck'), ('waist', 'waist'), ('head', 'head')], default='none', max_length=16),
        ),
    ]
