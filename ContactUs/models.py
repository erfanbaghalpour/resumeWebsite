from django.db import models


class ContactUs(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=300)
    text = models.TextField(max_length=2000)

    def __str__(self):
        return self.name
