# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-03-27 04:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='alamat',
        ),
        migrations.RemoveField(
            model_name='post',
            name='date',
        ),
        migrations.RemoveField(
            model_name='post',
            name='email',
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
