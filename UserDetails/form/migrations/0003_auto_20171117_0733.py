# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0002_auto_20171117_0543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercategory',
            name='state',
            field=models.CharField(max_length=50, choices=[(b'Telangana', b'TG'), (b'Andhra Pradesh', b'AP'), (b'Madhra Pradesh', b'MP')]),
        ),
    ]
