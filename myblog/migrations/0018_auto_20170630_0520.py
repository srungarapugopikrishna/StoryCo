# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0017_auto_20170630_0520'),
    ]

    operations = [
        migrations.RenameField(
            model_name='story',
            old_name='genreID',
            new_name='genre_id',
        ),
    ]
