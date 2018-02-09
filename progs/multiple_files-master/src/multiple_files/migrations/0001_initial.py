# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-19 11:17
from __future__ import unicode_literals

from django.db import migrations, models
import multiple_files.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parent_id', models.CharField(max_length=18)),
                ('file_name', models.CharField(max_length=100)),
                ('attachment', models.FileField(upload_to=multiple_files.models.upload_to)),
            ],
        ),
    ]