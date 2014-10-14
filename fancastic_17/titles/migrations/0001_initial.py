# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title_name', models.CharField(max_length=100)),
                ('released_year', models.IntegerField(null=True, blank=True)),
                ('plot', models.TextField()),
                ('title_type', models.CharField(default=b'movie', max_length=10, choices=[(b'movie', b'movie'), (b'tvshow', b'tvshow'), (b'miniseries', b'miniseries'), (b'musical', b'musical'), (b'animation', b'animation'), (b'short', b'short')])),
                ('status', models.CharField(default=b'announced', max_length=20, choices=[(b'announced', b'announced'), (b'pre-production', b'pre-production'), (b'filming', b'filming'), (b'post-production', b'post-production'), (b'released', b'released')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
