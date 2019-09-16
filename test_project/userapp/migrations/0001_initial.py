# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, null=True, blank=True)),
                ('gender', models.CharField(blank=True, max_length=100, null=True, choices=[(b'Male', b'Male'), (b'Female', b'Female'), (b'Others', b'Others')])),
                ('dob', models.DateField(max_length=50, null=True, blank=True)),
            ],
        ),
    ]
