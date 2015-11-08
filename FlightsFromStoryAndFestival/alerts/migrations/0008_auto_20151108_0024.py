# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alerts', '0007_auto_20151006_2019'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('registeredTime', models.DateTimeField(auto_now_add=True)),
                ('username', models.CharField(max_length=100)),
                ('pwd', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, blank=True)),
                ('token', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ('username',),
            },
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('placeName', models.CharField(max_length=100)),
                ('timeVisited', models.DateTimeField()),
                ('timeLeft', models.DateTimeField()),
            ],
            options={
                'ordering': ('placeName',),
            },
        ),
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('lastEditTime', models.DateTimeField(auto_now_add=True)),
                ('liked', models.IntegerField()),
                ('generated', models.IntegerField()),
            ],
            options={
                'ordering': ('lastEditTime', 'title'),
            },
        ),
        migrations.AlterUniqueTogether(
            name='story',
            unique_together=set([('title', 'lastEditTime')]),
        ),
        migrations.AddField(
            model_name='place',
            name='story',
            field=models.ForeignKey(related_name='places', to='alerts.Story'),
        ),
        migrations.AddField(
            model_name='customer',
            name='story',
            field=models.ForeignKey(related_name='customer', to='alerts.Story'),
        ),
    ]
