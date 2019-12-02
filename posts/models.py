from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=54, default='New Post')
    author = models.CharField(max_length=16, default="Anonymous")
    text = models.TextField()

    def __str__(self):
        return self.title