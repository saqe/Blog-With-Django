from django.contrib import admin
from .models import Post,PostTag

# Register PostTags Post model for admin dashboard.
admin.site.register(PostTag)
admin.site.register(Post)