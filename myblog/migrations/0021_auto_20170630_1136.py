# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0020_auto_20170630_0556'),
    ]

    operations = [
        migrations.RenameField(
            model_name='genres',
            old_name='genre',
            new_name='genre_id',
        ),
        migrations.AlterField(
            model_name='story',
            name='genre_id',
            field=models.ForeignKey(default=None, to='myblog.Genres'),
        ),
    ]
