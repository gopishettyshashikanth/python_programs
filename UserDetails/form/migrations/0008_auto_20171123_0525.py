# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0007_auto_20171123_0509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercategory',
            name='deptID',
            field=models.ForeignKey(blank=True, to='form.Dept', null=True),
        ),
        migrations.AlterField(
            model_name='usercategory',
            name='phone_number',
            field=models.CharField(unique=True, max_length=10, validators=[django.core.validators.RegexValidator(b'^[0-9]*$', b'Only numeric characters are allowed.')]),
        ),
    ]
