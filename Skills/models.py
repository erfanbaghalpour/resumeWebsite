from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from .validators import max_value_validator, min_value_validator
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


class Skill(models.Model):
    title = models.CharField(max_length=120)
    percent = models.IntegerField(validators=[max_value_validator,
                                              min_value_validator])

    def __str__(self):
        return self.title


class Biography(models.Model):
    title = models.CharField(max_length=120)
    name = models.CharField(max_length=120, blank=True, null=True)
    job = models.CharField(max_length=120, blank=True, null=True)
    # description = RichTextUploadingField(max_length=2000)
    description = models.TextField(max_length=2000)
    image = models.ImageField(max_length=1000, upload_to='media/images/biography')
    is_active = models.BooleanField()

    def __str__(self):
        return self.title


# class Experience(models.Model):
#     title = models.CharField(max_length=10, null=True, blank=True)
#     projects_count = models.IntegerField()
#     lines_of_code = models.IntegerField()
#     working_hours = models.IntegerField()
#     rates = models.IntegerField()

# def __str__(self):
#     return self.title


class Experience(models.Model):
    projects_count = models.IntegerField()
    lines_of_code = models.IntegerField()
    working_hours = models.IntegerField()
    rates = models.IntegerField()

    def __str__(self):
        return f'Experience:{self.id}'
