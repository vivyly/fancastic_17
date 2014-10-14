# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import common.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Professional',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.SlugField()),
                ('fullname', models.CharField(max_length=100, blank=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated', common.models.AutoDateTimeField(default=django.utils.timezone.now)),
                ('height', models.CharField(max_length=10, blank=True)),
                ('is_alive', models.BooleanField(default=True)),
                ('is_active', models.BooleanField(default=True)),
                ('birthday', models.IntegerField(null=True, blank=True)),
                ('birthmonth', models.IntegerField(null=True, blank=True)),
                ('birthyear', models.IntegerField(null=True, blank=True)),
                ('nationality', models.CharField(max_length=100, blank=True)),
                ('url', models.URLField(blank=True)),
                ('imdb', models.URLField(blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
