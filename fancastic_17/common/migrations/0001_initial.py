# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.SlugField(unique=True)),
                ('created', models.DateTimeField()),
                ('updated', models.DateTimeField()),
                ('ip', models.IPAddressField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
