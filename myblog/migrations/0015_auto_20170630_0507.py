# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0014_auto_20170630_0458'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='story',
            name='genre_id',
        ),
        migrations.AddField(
            model_name='story',
            name='genreID',
            field=models.ForeignKey(default=uuid.uuid4, to='myblog.Genres'),
        ),
    ]
