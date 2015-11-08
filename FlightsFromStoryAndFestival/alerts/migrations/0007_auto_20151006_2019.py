# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alerts', '0006_alertaction'),
    ]

    operations = [
        migrations.AddField(
            model_name='useralert',
            name='frequency',
            field=models.FloatField(default=60),
        ),
        migrations.AddField(
            model_name='useralert',
            name='last_triggered',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='useralert',
            name='status',
            field=models.CharField(default=b'active', max_length=10, choices=[(b'active', b'ACTIVE'), (b'disabled', b'DISABLED')]),
        ),
        migrations.AlterField(
            model_name='useralert',
            name='alert_expression',
            field=models.CharField(max_length=50),
        ),
    ]
