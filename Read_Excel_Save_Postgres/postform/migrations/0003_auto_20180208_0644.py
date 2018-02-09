# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('postform', '0002_auto_20180208_0642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='active_membership_id',
            field=models.CharField(max_length=80, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='details',
            name='amount',
            field=models.CharField(max_length=80, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='details',
            name='assembly_code',
            field=models.CharField(max_length=80, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='details',
            name='caste',
            field=models.CharField(max_length=80, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='details',
            name='colony',
            field=models.CharField(max_length=80, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='details',
            name='dno',
            field=models.CharField(max_length=80, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='details',
            name='email',
            field=models.CharField(max_length=80, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='details',
            name='gender',
            field=models.CharField(max_length=80, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='details',
            name='mandal',
            field=models.CharField(max_length=80, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='details',
            name='membership_id',
            field=models.CharField(max_length=80, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='details',
            name='mobile_number',
            field=models.CharField(max_length=80, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='details',
            name='name',
            field=models.CharField(max_length=80, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='details',
            name='pincode',
            field=models.CharField(max_length=80, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='details',
            name='remark',
            field=models.CharField(max_length=80, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='details',
            name='s_w_d_of',
            field=models.CharField(max_length=80, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='details',
            name='street',
            field=models.CharField(max_length=80, null=True, blank=True),
        ),
    ]
