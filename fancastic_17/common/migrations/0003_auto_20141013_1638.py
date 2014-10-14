# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_basemodel_creator'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basemodel',
            name='creator',
        ),
        migrations.DeleteModel(
            name='BaseModel',
        ),
    ]
