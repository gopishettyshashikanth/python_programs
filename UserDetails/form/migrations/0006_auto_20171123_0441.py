# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0005_auto_20171121_0736'),
    ]

    operations = [
        migrations.AddField(
            model_name='usercategory',
            name='mobile',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='usercategory',
            name='deptID',
            field=models.ForeignKey(blank=True, to='form.Dept', null=True),
        ),
    ]
