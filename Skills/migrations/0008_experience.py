# Generated by Django 5.0.1 on 2024-01-15 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Skills', '0007_alter_biography_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projects_count', models.IntegerField()),
                ('lines_of_code', models.IntegerField()),
                ('working_hours', models.IntegerField()),
                ('rates', models.IntegerField()),
            ],
        ),
    ]
