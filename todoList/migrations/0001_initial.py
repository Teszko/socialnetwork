# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-08 17:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('todo_text', models.CharField(max_length=159)),
                ('deadline_date', models.DateTimeField(verbose_name='date published')),
                ('percentage', models.IntegerField(default=0)),
            ],
        ),
    ]
