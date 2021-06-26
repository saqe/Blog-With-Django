from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify

class PostTag(models.Model):
    tag = models.CharField(max_length = 30)

    def __str__(self):
        return self.tag
    
class Post(models.Model):
    slug = models.SlugField(max_length=255,unique=True,db_index=True,)
    title = models.CharField(max_length = 255)
    posted_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)
    content = models.TextField()
    
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # (Optional) A single post can have mutliple tags.
    tags = models.ManyToManyField(PostTag,blank=True)

    featured  = models.BooleanField(default=False)
    published = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-posted_datetime']
        
    def __str__(self):
        return self.title

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.slug:
            self.slug = slugify(self.title)

        return super(Post,self)\
            .save(
                force_insert=force_insert,
                force_update=force_update,
                using=using,
                update_fields=update_fields
            )

    # After creating a post, user will be redirected to that post.
    def get_absolute_url(self):
        return reverse("view-blog-post", kwargs={"slug": self.slug})