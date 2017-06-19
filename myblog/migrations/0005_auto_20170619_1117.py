# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0004_editor'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Editor',
        ),
        migrations.RenameField(
            model_name='story',
            old_name='Title',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='story',
            name='Story',
        ),
        migrations.AddField(
            model_name='story',
            name='text',
            field=tinymce.models.HTMLField(default=datetime.datetime(2017, 6, 19, 11, 17, 22, 893204, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
