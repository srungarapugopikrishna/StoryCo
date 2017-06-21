# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0008_remove_story_textarea'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='story',
            name='id',
        ),
        migrations.AddField(
            model_name='story',
            name='story_id',
            field=models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True),
        ),
    ]
