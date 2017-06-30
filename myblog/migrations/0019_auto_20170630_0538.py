# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0018_auto_20170630_0520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='genre_id',
            field=models.ForeignKey(to='myblog.Genres'),
        ),
    ]
