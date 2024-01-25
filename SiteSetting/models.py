from django.db import models


class Setting(models.Model):
    email = models.EmailField()
    copy_right_text = models.CharField(max_length=200)
    address = models.CharField(max_length=400)
    phone_number = models.CharField(max_length=11)

    def __str__(self):
        return self.email


class SocialMedia(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField()
    SOCIAL_MEDIA_ICON = [
        ('linkedin-square', 'icon linkedin'),
        ('instagram-logo', 'icon instagram'),
        ('telegram', 'icon telegram'),
        ('envelope', 'icon envelope'),
    ]
    icon = models.CharField(max_length=15, choices=SOCIAL_MEDIA_ICON)

    def __str__(self):
        return self.title
