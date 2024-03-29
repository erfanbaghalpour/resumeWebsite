# Generated by Django 5.0.1 on 2024-01-25 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SiteSetting', '0003_alter_socialmedia_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialmedia',
            name='icon',
            field=models.CharField(choices=[('linkedin-square', 'icon linkedin'), ('instagram-logo', 'icon instagram'), ('telegram', 'icon telegram'), ('envelope', 'icon envelope'), ('github-square', 'icon github')], max_length=15),
        ),
    ]
