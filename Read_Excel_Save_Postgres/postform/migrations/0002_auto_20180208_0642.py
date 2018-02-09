# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('postform', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='village',
            field=models.CharField(max_length=80, null=True, blank=True),
        ),
    ]
