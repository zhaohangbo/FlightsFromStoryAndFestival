# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alerts', '0005_auto_20150818_2043'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlertAction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('alert_choice', models.CharField(default=b'email', max_length=5, choices=[(b'email', b'EMAIL'), (b'api', b'API'), (b'sms', b'SMS'), (b'slack', b'SLACK'), (b'pager', b'PAGER')])),
                ('action_email', models.EmailField(max_length=254, blank=True)),
                ('action_api_url', models.URLField(blank=True)),
                ('action_payload', models.TextField(blank=True)),
                ('alert', models.ForeignKey(related_name='actions', to='alerts.UserAlert')),
            ],
            options={
                'ordering': ('alert',),
            },
        ),
    ]
