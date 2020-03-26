# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-03-26 06:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='email',
            field=models.EmailField(default='nama@mail.com', max_length=254),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
