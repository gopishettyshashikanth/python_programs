# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0006_auto_20171117_0744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercategory',
            name='salary',
            field=models.IntegerField(),
        ),
    ]
