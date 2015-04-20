# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0007_auto_20150419_2222'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='performer',
            options={'ordering': ('program', 'order')},
        ),
    ]
