# Generated by Django 5.0.1 on 2024-02-05 19:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Comments', '0005_reply_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reply',
            name='blog',
        ),
    ]