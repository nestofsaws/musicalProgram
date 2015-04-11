# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('artistid', models.CharField(unique=True, max_length=12)),
                ('url', models.CharField(max_length=200, unique=True, null=True)),
            ],
            options={
                'ordering': ('last_name', 'first_name'),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=50)),
                ('key', models.CharField(max_length=50, null=True)),
                ('language', models.CharField(max_length=50, null=True)),
                ('date', models.CharField(max_length=50, null=True)),
                ('instrumentation', models.CharField(max_length=50, null=True)),
                ('description', models.CharField(default=b'', max_length=200)),
                ('composers', models.ManyToManyField(to='programs.Artist')),
            ],
            options={
                'ordering': ('title', 'date'),
                'verbose_name_plural': 'Songs',
            },
            bases=(models.Model,),
        ),
    ]
