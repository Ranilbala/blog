# Generated by Django 4.1.5 on 2023-02-02 19:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='date',
            new_name='creation_time',
        ),
    ]
