# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2020-07-28 08:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('age', models.IntegerField(max_length=11)),
            ],
            options={
                'db_table': 'student',
            },
        ),
    ]
