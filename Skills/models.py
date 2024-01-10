from django.db import models


class Skill(models.Model):
    title = models.CharField(max_length=120)
    percent = models.IntegerField()

    def __str__(self):
        return self.title


class Biography(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(max_length=1000)
    image = models.ImageField(max_length=1000, upload_to='media/images/biography')
    is_active = models.BooleanField()

    def __str__(self):
        return self.title
