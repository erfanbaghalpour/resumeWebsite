# Generated by Django 5.0.1 on 2024-02-08 19:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Comments', '0009_rename_comment_reply_comment_org'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reply',
            name='blog',
        ),
    ]
