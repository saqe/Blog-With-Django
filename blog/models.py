from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
class PostTag(models.Model):
    tag = models.CharField(max_length = 30)

    def __str__(self):
        return self.tag
    
class Post(models.Model):
    title = models.CharField(max_length = 255)
    posted_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)
    content = models.TextField()
    
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # (Optional) A single post can have mutliple tags.
    tags = models.ManyToManyField(PostTag,blank=True)
    published = models.BooleanField(default=False)
    def __str__(self):
        return self.title
    
    # After creating a post, user will be redirected to that post.
    def get_absolute_url(self):
        return reverse("view-blog-post", kwargs={"pk": self.pk})
    