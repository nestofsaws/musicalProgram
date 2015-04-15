# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0002_auto_20150411_2119'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artist',
            name='artistid',
        ),
        migrations.RemoveField(
            model_name='song',
            name='songid',
        ),
    ]
