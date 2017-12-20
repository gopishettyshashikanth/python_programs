# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='dept',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('deptName', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='UserCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('Email', models.CharField(max_length=20)),
                ('salary', models.IntegerField()),
                ('tds', models.CharField(max_length=20)),
                ('status', models.BooleanField(default=False)),
                ('gender', models.CharField(max_length=10, choices=[(b'Male', b'Male'), (b'Female', b'Female')])),
                ('state', models.CharField(max_length=50, choices=[(b'Telangana', b'TG'), (b'Andhra Pradesh', b'AP'), (b'Madhra Pradesh', b'MP')])),
                ('deptID', models.ForeignKey(blank=True, to='form.dept', null=True)),
            ],
        ),
    ]
