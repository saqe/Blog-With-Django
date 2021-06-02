from django.contrib import admin
from .models import Post

# Register Post model for admin dashboard.
admin.site.register(Post)