# Generated by Django 4.1.5 on 2023-02-02 19:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_rename_creation_time_post_date_post_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='date',
        ),
        migrations.RemoveField(
            model_name='post',
            name='time',
        ),
        migrations.AddField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
