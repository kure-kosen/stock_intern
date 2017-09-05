# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-06 00:36
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
import markdownx.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='non title', max_length=128)),
                ('text', markdownx.models.MarkdownxField()),
                ('created', models.DateTimeField(default=datetime.datetime.now)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=128)),
                ('created', models.DateTimeField(default=datetime.datetime.now)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='category_id',
            field=models.ForeignKey(db_column='category_id', on_delete=django.db.models.deletion.CASCADE, to='articles.Category'),
        ),
        migrations.AddField(
            model_name='article',
            name='user_id',
            field=models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, to='accounts.User'),
        ),
    ]
