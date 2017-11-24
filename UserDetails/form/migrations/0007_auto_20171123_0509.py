# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0006_auto_20171123_0441'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usercategory',
            old_name='mobile',
            new_name='phone_number',
        ),
        migrations.AlterField(
            model_name='usercategory',
            name='deptID',
            field=models.ForeignKey(blank=True, to='form.Dept', null=True),
        ),
    ]
