# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
import tinymce.models
from django.conf import settings
import django.core.validators
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.UUIDField(default=uuid.uuid4, serialize=False, primary_key=True)),
                ('category_label', models.CharField(max_length=50)),
                ('category_description', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='ContentType',
            fields=[
                ('content_id', models.UUIDField(default=uuid.uuid4, serialize=False, primary_key=True)),
                ('content_type', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('episode_id', models.UUIDField(default=uuid.uuid4, serialize=False, primary_key=True)),
                ('episode_description', models.CharField(max_length=500)),
                ('episode_content', tinymce.models.HTMLField()),
                ('episode_content_relative_url', models.CharField(max_length=500, validators=[django.core.validators.URLValidator()])),
                ('categories', models.CharField(max_length=500)),
                ('pub_date', models.DateTimeField(default=datetime.datetime.now, blank=True)),
                ('created_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('episode_content_type', models.ForeignKey(default=None, to='myblog.ContentType', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Genres',
            fields=[
                ('genre_id', models.UUIDField(default=uuid.uuid4, serialize=False, primary_key=True)),
                ('genre_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('item_id', models.UUIDField(default=uuid.uuid4, serialize=False, primary_key=True)),
                ('item_title', models.CharField(max_length=500)),
                ('item_description', models.CharField(max_length=1000)),
                ('pub_date', models.DateTimeField(default=datetime.datetime.now, blank=True)),
                ('created_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MainItem',
            fields=[
                ('mainItem_id', models.UUIDField(default=uuid.uuid4, serialize=False, primary_key=True)),
                ('mainItem_title', models.CharField(max_length=500)),
                ('mainItem_description', models.CharField(max_length=500)),
                ('pub_date', models.DateTimeField(default=datetime.datetime.now, blank=True)),
                ('created_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Relations',
            fields=[
                ('relation_id', models.UUIDField(default=uuid.uuid4, serialize=False, primary_key=True)),
                ('parent_id', models.CharField(max_length=500)),
                ('child_id', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Relationship',
            fields=[
                ('relation_id', models.UUIDField(default=uuid.uuid4, serialize=False, primary_key=True)),
                ('parent_id', models.CharField(max_length=500)),
                ('child_id', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='RepresentationType',
            fields=[
                ('representation_id', models.UUIDField(default=uuid.uuid4, serialize=False, primary_key=True)),
                ('representation_type', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Story',
            fields=[
                ('story_id', models.UUIDField(default=uuid.uuid4, serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=500)),
                ('text', tinymce.models.HTMLField()),
                ('pub_date', models.DateTimeField(default=datetime.datetime.now, blank=True)),
                ('created_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('genre_id', models.ForeignKey(default=None, blank=True, to='myblog.Genres')),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='item_type',
            field=models.ForeignKey(default=None, to='myblog.RepresentationType', null=True),
        ),
        migrations.AddField(
            model_name='episode',
            name='episode_type',
            field=models.ForeignKey(default=None, to='myblog.RepresentationType', null=True),
        ),
    ]
