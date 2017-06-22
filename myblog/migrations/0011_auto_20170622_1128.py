# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0010_auto_20170621_0747'),
    ]

    operations = [
        migrations.CreateModel(
            name='relations',
            fields=[
                ('relation_id', models.UUIDField(serialize=False, primary_key=True)),
                ('parent_id', models.CharField(max_length=500)),
                ('child_id', models.CharField(max_length=500)),
            ],
        ),
        migrations.AlterField(
            model_name='story',
            name='story_id',
            field=models.UUIDField(serialize=False, primary_key=True),
        ),
    ]
