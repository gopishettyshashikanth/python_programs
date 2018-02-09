# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='details',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, null=True, blank=True)),
                ('s_w_d_of', models.CharField(max_length=50, null=True, blank=True)),
                ('gender', models.CharField(max_length=50, null=True, blank=True)),
                ('caste', models.CharField(max_length=50, null=True, blank=True)),
                ('dno', models.CharField(max_length=50, null=True, blank=True)),
                ('street', models.CharField(max_length=50, null=True, blank=True)),
                ('colony', models.CharField(max_length=50, null=True, blank=True)),
                ('village', models.CharField(max_length=50, null=True, blank=True)),
                ('pincode', models.CharField(max_length=50, null=True, blank=True)),
                ('mandal', models.CharField(max_length=50, null=True, blank=True)),
                ('assembly_code', models.CharField(max_length=50, null=True, blank=True)),
                ('membership_id', models.CharField(max_length=50, null=True, blank=True)),
                ('active_membership_id', models.CharField(max_length=50, null=True, blank=True)),
                ('mobile_number', models.CharField(max_length=50, null=True, blank=True)),
                ('email', models.CharField(max_length=50, null=True, blank=True)),
                ('amount', models.CharField(max_length=50, null=True, blank=True)),
                ('remark', models.CharField(max_length=50, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='fileupload',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('file', models.FileField(upload_to=b'documents/')),
            ],
        ),
        migrations.CreateModel(
            name='userDetails',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
            ],
        ),
    ]
