# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0002_story_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime.now, blank=True),
        ),
    ]
