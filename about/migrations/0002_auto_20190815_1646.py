# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-08-15 09:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nilai',
            name='nama',
        ),
        migrations.RemoveField(
            model_name='spp',
            name='nama',
        ),
    ]