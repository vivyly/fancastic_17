# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import common.models


class Migration(migrations.Migration):

    dependencies = [
        ('titles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adaptation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.SlugField()),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated', common.models.AutoDateTimeField(default=django.utils.timezone.now)),
                ('adaptation_name', models.CharField(max_length=255)),
                ('release_year', models.IntegerField(null=True, blank=True)),
                ('rights_owner', models.CharField(max_length=255)),
                ('plot', models.TextField(blank=True)),
                ('adapt_media', models.CharField(default=b'movie', max_length=10, choices=[(b'movie', b'movie'), (b'tvshow', b'tvshow'), (b'miniseries', b'miniseries'), (b'musical', b'musical'), (b'animation', b'animation'), (b'short', b'short')])),
                ('adapt_type', models.CharField(default=b'remake', max_length=20, choices=[(b'remake', b'remake'), (b'sequel', b'sequel'), (b'prequel', b'prequel'), (b'spinoff', b'spinoff'), (b'alternate', b'alternate'), (b'original', b'original'), (b'inspired', b'inspired')])),
                ('status', models.CharField(default=b'announced', max_length=20, choices=[(b'rumored', b'rumored'), (b'announced', b'announced'), (b'pre-production', b'pre-production'), (b'filming', b'filming'), (b'post-production', b'post-production'), (b'released', b'released')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SourceMaterial',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.SlugField()),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated', common.models.AutoDateTimeField(default=django.utils.timezone.now)),
                ('source_name', models.CharField(max_length=255)),
                ('source_creator', models.CharField(max_length=100, blank=True)),
                ('released_year', models.IntegerField(null=True, blank=True)),
                ('plot', models.TextField(blank=True)),
                ('source_type', models.CharField(default=b'book', max_length=10, choices=[(b'book', b'book'), (b'comic', b'comic'), (b'cartoon', b'cartoon'), (b'anime', b'anime'), (b'movie', b'movie'), (b'tvshow', b'tvshow'), (b'musical', b'musical'), (b'parkride', b'parkride'), (b'boardgame', b'boardgame'), (b'videogame', b'videogame'), (b'mythology', b'mythology')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='Title',
        ),
        migrations.AddField(
            model_name='adaptation',
            name='source_material',
            field=models.ForeignKey(to='titles.SourceMaterial', null=True),
            preserve_default=True,
        ),
    ]
