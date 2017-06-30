# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0016_auto_20170630_0514'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='story',
            name='gid',
        ),
        migrations.AddField(
            model_name='story',
            name='genreID',
            field=models.ForeignKey(default=uuid.uuid4, to='myblog.Genres'),
        ),
    ]
