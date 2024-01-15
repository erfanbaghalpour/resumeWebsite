from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from .validators import max_value_validator, min_value_validator


class Skill(models.Model):
    title = models.CharField(max_length=120)
    percent = models.IntegerField(validators=[max_value_validator,
                                              min_value_validator])

    def __str__(self):
        return self.title


class Biography(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(max_length=1000)
    image = models.ImageField(max_length=1000, upload_to='media/images/biography')
    is_active = models.BooleanField()

    def __str__(self):
        return self.title
