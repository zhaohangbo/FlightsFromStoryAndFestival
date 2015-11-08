# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ZeusUserAlertRules',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('username', models.CharField(max_length=100)),
                ('token', models.CharField(max_length=100)),
                ('metric_key', models.CharField(max_length=100)),
                ('metric_threshold', models.CharField(max_length=100)),
                ('metric_timeperiod', models.CharField(default=b'', max_length=100, blank=True)),
                ('metric_evaluator', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
