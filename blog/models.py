from django.db import models
from django.contrib.auth.models import User

from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length = 255)
    posted_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)
    content = models.TextField()
    
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title