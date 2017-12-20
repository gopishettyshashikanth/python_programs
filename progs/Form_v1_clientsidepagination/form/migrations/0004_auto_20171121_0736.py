# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0003_auto_20171121_0721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercategory',
            name='deptID',
            field=models.ForeignKey(choices=[(b'CSE', b'10'), (b'ECE', b'20')], to='form.Dept', blank=True, null=True),
        ),
    ]
