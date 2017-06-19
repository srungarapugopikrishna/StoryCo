# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import tinymce.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0006_story_created_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='textArea',
            field=tinymce.models.HTMLField(default='default'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='story',
            name='created_by',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
