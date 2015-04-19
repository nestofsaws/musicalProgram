# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0004_auto_20150415_2325'),
    ]

    operations = [
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=75)),
                ('location', models.CharField(max_length=100)),
                ('date', models.DateField(null=True, blank=True)),
                ('secondary_artist', models.CharField(max_length=100, null=True, blank=True)),
                ('artist', models.ManyToManyField(to='programs.Artist', null=True, blank=True)),
                ('songs', models.ManyToManyField(to='programs.Song')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='song',
            name='performers',
        ),
        migrations.AddField(
            model_name='artist',
            name='photo',
            field=models.ImageField(null=True, upload_to=b'artist/photo/', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='song',
            name='composer',
            field=models.CharField(max_length=50, null=True, blank=True),
            preserve_default=True,
        ),
    ]
