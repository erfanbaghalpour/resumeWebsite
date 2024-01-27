from django.db import models


class MyServices(models.Model):
    title = models.CharField(max_length=300)
    image_icon = models.ImageField(max_length=1000)
    text = models.TextField(max_length=1000)

    def __str__(self):
        return self.title
