# Generated by Django 5.0.1 on 2024-01-15 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Skills', '0006_alter_biography_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='biography',
            name='description',
            field=models.TextField(max_length=2000),
        ),
    ]
