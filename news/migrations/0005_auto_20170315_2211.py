# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-15 22:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20170315_2210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(upload_to='news'),
        ),
    ]