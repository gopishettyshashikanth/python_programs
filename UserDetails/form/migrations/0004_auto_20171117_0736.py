# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0003_auto_20171117_0733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercategory',
            name='salary',
            field=models.IntegerField(max_length=20),
        ),
    ]
