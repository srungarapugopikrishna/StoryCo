# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0013_story_genre_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='genre_id',
            field=models.ForeignKey(related_name='genreID', default=uuid.uuid4, to='myblog.Genres'),
        ),
    ]
