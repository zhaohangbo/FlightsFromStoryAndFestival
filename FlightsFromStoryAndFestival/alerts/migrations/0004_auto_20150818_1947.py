# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alerts', '0003_auto_20150731_0622'),
    ]

    operations = [
        migrations.RenameField(
            model_name='useralert',
            old_name='metric_name',
            new_name='alert_expression',
        ),
        migrations.RemoveField(
            model_name='useralert',
            name='metric_timeperiod',
        ),
        migrations.AddField(
            model_name='alertrule',
            name='metric_name',
            field=models.CharField(default='some_metric_name', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='alertrule',
            name='metric_timeperiod',
            field=models.CharField(default=b'', max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='alertrule',
            name='rule_name',
            field=models.CharField(default='some_rule_name_like_R1', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='alertrule',
            name='stats_function_operator',
            field=models.CharField(default=b'val', max_length=3, choices=[(b'avg', b'AVERAGE'), (b'max', b'MAXIMUM'), (b'min', b'MINIMUM'), (b'val', b'VALUE')]),
        ),
        migrations.AddField(
            model_name='useralert',
            name='alert_name',
            field=models.CharField(default='some_alert_name', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='useralert',
            name='alert_severity',
            field=models.CharField(default=b'S1', max_length=2, choices=[(b'S1', b'CRITICAL'), (b'S2', b'MAJOR'), (b'S3', b'MODERATE'), (b'S4', b'MINOR'), (b'S5', b'INFORMATION')]),
        ),
    ]
