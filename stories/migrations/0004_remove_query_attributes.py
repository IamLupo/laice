# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-22 22:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0003_auto_20161022_1455'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='query',
            name='attributes',
        ),
    ]
