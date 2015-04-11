# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='songid',
            field=models.CharField(default=b'', unique=True, max_length=12),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='song',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]
