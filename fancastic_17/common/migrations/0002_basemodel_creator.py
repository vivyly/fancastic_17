# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fan', '0001_initial'),
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='basemodel',
            name='creator',
            field=models.ForeignKey(to='fan.FanUser'),
            preserve_default=True,
        ),
    ]
