# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0019_auto_20170630_0538'),
    ]

    operations = [
        migrations.RenameField(
            model_name='genres',
            old_name='genre_id',
            new_name='genre',
        ),
    ]
