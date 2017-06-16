# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 14, 9, 32, 52, 894900, tzinfo=utc), verbose_name=b'date published'),
            preserve_default=False,
        ),
    ]
