# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0012_auto_20170629_0850'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='genre_id',
            field=models.ForeignKey(default=uuid.uuid4, to='myblog.Genres'),
        ),
    ]
