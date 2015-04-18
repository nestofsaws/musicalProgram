# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0003_auto_20150415_1908'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='song',
            options={'ordering': ('title',)},
        ),
        migrations.RenameField(
            model_name='song',
            old_name='composers',
            new_name='performers',
        ),
        migrations.RemoveField(
            model_name='song',
            name='date',
        ),
        migrations.RemoveField(
            model_name='song',
            name='description',
        ),
        migrations.RemoveField(
            model_name='song',
            name='instrumentation',
        ),
        migrations.AddField(
            model_name='song',
            name='composed_on',
            field=models.IntegerField(max_length=4, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='artist',
            name='url',
            field=models.URLField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='song',
            name='key',
            field=models.CharField(max_length=10, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='song',
            name='language',
            field=models.CharField(max_length=50, null=True, blank=True),
            preserve_default=True,
        ),
    ]
