# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myblog', '0005_auto_20170619_1117'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='created_by',
            field=models.ForeignKey(blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
