from rest_framework import viewsets,permissions
from .serializers import BlogSerializer
from blog.models import Post

class BlogViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [permissions.IsAuthenticated]