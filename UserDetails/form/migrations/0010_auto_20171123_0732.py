# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0009_auto_20171123_0531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercategory',
            name='deptID',
            field=models.ForeignKey(blank=True, to='form.Dept', null=True),
        ),
    ]
