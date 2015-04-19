# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0005_auto_20150419_1636'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='program',
            options={'ordering': ('date', 'title')},
        ),
    ]
