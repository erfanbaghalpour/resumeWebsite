from django.db import models
from django.contrib.auth.models import User


class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE )
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=5000)
    image = models.ImageField(max_length=1000)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.author
