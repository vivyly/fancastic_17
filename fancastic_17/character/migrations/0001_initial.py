# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('titles', '0002_auto_20141013_2232'),
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('character_name', models.CharField(max_length=100)),
                ('character_status', models.CharField(default=b'source', max_length=10, choices=[(b'original', b'original'), (b'unknown', b'unknown'), (b'rumored', b'rumored'), (b'source', b'source')])),
                ('title', models.ForeignKey(to='titles.Adaptation')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
