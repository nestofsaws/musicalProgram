# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0006_auto_20150419_1740'),
    ]

    operations = [
        migrations.CreateModel(
            name='Performer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('role', models.CharField(max_length=100, null=True, blank=True)),
                ('order', models.IntegerField(default=0)),
                ('artist', models.ForeignKey(to='programs.Artist')),
                ('program', models.ForeignKey(to='programs.Program')),
            ],
            options={
                'ordering': ('program', '-order'),
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='program',
            name='artist',
        ),
        migrations.RemoveField(
            model_name='program',
            name='secondary_artist',
        ),
        migrations.AddField(
            model_name='program',
            name='performers',
            field=models.ManyToManyField(to='programs.Artist', through='programs.Performer'),
            preserve_default=True,
        ),
    ]
