# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('postgresdb', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='form',
            old_name='Gender',
            new_name='gender',
        ),
        migrations.RenameField(
            model_name='form',
            old_name='Location',
            new_name='location',
        ),
    ]
