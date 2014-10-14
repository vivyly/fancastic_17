# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import common.models


class Migration(migrations.Migration):

    dependencies = [
        ('fan', '0002_auto_20141013_2232'),
        ('professional', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FanCast',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated', common.models.AutoDateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(default=b'unknown', max_length=10, choices=[(b'unknown', b'unknown'), (b'rumored', b'rumored'), (b'negotiation', b'negotiation'), (b'confirmed', b'confirmed'), (b'rejected', b'rejected'), (b'replaced', b'replaced')])),
                ('creator', models.ForeignKey(to='fan.FanUser')),
                ('professional', models.ForeignKey(to='professional.Professional')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
