# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0015_auto_20170630_0507'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='story',
            name='genreID',
        ),
        migrations.AddField(
            model_name='story',
            name='gid',
            field=models.ForeignKey(related_name='genres_story', default=uuid.uuid4, to='myblog.Genres'),
        ),
    ]
