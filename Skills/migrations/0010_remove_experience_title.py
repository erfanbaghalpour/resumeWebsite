# Generated by Django 5.0.1 on 2024-01-15 17:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Skills', '0009_experience_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='experience',
            name='title',
        ),
    ]