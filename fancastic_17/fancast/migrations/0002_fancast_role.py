# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('role', '0001_initial'),
        ('fancast', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fancast',
            name='role',
            field=models.ForeignKey(to='role.Role'),
            preserve_default=True,
        ),
    ]
