# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2020-07-28 06:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('interface', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('desc', models.CharField(max_length=255, null=True)),
                ('uri', models.CharField(max_length=116)),
                ('header', models.CharField(max_length=255, null=True)),
                ('body', models.CharField(max_length=255, null=True)),
                ('r_type', models.CharField(max_length=255)),
                ('result', models.CharField(max_length=255)),
                ('interface', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interface.Interface')),
            ],
            options={
                'db_table': 'case',
            },
        ),
    ]
