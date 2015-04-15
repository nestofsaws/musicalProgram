# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0003_auto_20150415_2317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='performers',
            field=models.ManyToManyField(to='programs.Artist', null=True, blank=True),
            preserve_default=True,
        ),
    ]
