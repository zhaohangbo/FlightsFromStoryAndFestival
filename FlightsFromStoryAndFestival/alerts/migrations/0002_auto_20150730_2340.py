# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alerts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlertRule',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('metric_name', models.CharField(max_length=100)),
                ('metric_key', models.CharField(max_length=100)),
                ('metric_threshold', models.CharField(max_length=100)),
                ('metric_timeperiod', models.CharField(default=b'', max_length=100, blank=True)),
                ('metric_evaluator', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ('alert',),
            },
        ),
        migrations.CreateModel(
            name='UserAlert',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('username', models.CharField(max_length=100)),
                ('token', models.CharField(max_length=100)),
                ('metric_name', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
        migrations.DeleteModel(
            name='ZeusUserAlertRules',
        ),
        migrations.AddField(
            model_name='alertrule',
            name='alert',
            field=models.ForeignKey(related_name='rules', to='alerts.UserAlert'),
        ),
        migrations.AlterUniqueTogether(
            name='alertrule',
            unique_together=set([('alert', 'metric_name', 'metric_key')]),
        ),
    ]
