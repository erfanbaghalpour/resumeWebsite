# Generated by Django 5.0.1 on 2024-01-24 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Skills', '0011_biography_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='biography',
            name='job',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
