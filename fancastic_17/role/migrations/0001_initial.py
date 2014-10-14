# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('titles', '0002_auto_20141013_2232'),
        ('character', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('role', models.CharField(default=b'Actor', max_length=20, choices=[(b'Director', b'Director'), (b'Writer', b'Writer'), (b'Producer', b'Producer'), (b'Music', b'Music'), (b'Cinematography', b'Cinematography'), (b'Crew', b'Crew'), (b'Actor', b'Actor')])),
                ('desc', models.TextField(blank=True)),
                ('url', models.URLField(blank=True)),
                ('imdb', models.URLField(blank=True)),
                ('character', models.ForeignKey(to='character.Character', null=True)),
                ('title', models.ForeignKey(to='titles.Adaptation')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
