# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0011_auto_20170622_1128'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genres',
            fields=[
                ('genre_id', models.UUIDField(default=uuid.uuid4, serialize=False, primary_key=True)),
                ('genre_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='relations',
            name='relation_id',
            field=models.UUIDField(default=uuid.uuid4, serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='story',
            name='story_id',
            field=models.UUIDField(default=uuid.uuid4, serialize=False, primary_key=True),
        ),
    ]
