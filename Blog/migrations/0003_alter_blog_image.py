# Generated by Django 5.0.1 on 2024-02-19 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0002_alter_blog_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(max_length=1000, upload_to='static_cdn/media'),
        ),
    ]