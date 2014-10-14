# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import common.models


class Migration(migrations.Migration):

    dependencies = [
        ('fan', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fanuser',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='fanuser',
            name='updated',
            field=common.models.AutoDateTimeField(default=django.utils.timezone.now),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='fanuser',
            name='slug',
            field=models.SlugField(),
        ),
    ]
