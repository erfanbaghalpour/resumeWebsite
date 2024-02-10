from django.db import models
from Blog.models import Blog


class Comment(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=500)
    text = models.TextField(max_length=5000)
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    parent = models.ForeignKey('Comment', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
        # return f"{self.id}, {self.blog.title}"


