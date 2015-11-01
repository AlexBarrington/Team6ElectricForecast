# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('electricForcastApp', '0002_auto_20151031_1942'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='username',
            field=models.TextField(default='adminUser'),
            preserve_default=False,
        ),
    ]
