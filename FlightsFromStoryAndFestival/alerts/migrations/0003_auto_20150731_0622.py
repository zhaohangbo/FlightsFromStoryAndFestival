# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alerts', '0002_auto_20150730_2340'),
    ]

    operations = [
        migrations.AddField(
            model_name='useralert',
            name='metric_timeperiod',
            field=models.CharField(default=b'', max_length=100, blank=True),
        ),
        migrations.AlterUniqueTogether(
            name='alertrule',
            unique_together=set([('alert', 'metric_key')]),
        ),
        migrations.RemoveField(
            model_name='alertrule',
            name='metric_name',
        ),
        migrations.RemoveField(
            model_name='alertrule',
            name='metric_timeperiod',
        ),
    ]
