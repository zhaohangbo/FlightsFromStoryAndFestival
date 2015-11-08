# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alerts', '0004_auto_20150818_1947'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='alertrule',
            unique_together=set([('alert', 'rule_name', 'metric_name', 'metric_key')]),
        ),
        migrations.AlterUniqueTogether(
            name='useralert',
            unique_together=set([('alert_name', 'username', 'token')]),
        ),
    ]
