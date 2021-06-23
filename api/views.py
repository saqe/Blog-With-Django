from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from rest_framework import (
    viewsets,
    views,
    permissions,
    generics,
    mixins)
from rest_framework.decorators import api_view,action,permission_classes
from rest_framework.response import Response

from .serializers import (
    BlogSerializer,
    FeaturedAndPublishedSerializer,
    UserSerializer,)
from blog.models import Post
from .permissions import IsOwnerOrReadOnly

class BlogViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsOwnerOrReadOnly]

    @action(detail=False,name='Get All Published Blog',permission_classes=[permissions.IsAuthenticated])
    def published(self, request):
        published_articles = Post.objects.filter(published=True)
        page = self.paginate_queryset(published_articles)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(published_articles, many=True)
        return Response(serializer.data)

    @action(detail=True,methods=['put','get'], name='Update BlogPost status',permission_classes=[permissions.IsAdminUser],serializer_class=FeaturedAndPublishedSerializer)
    def featured_and_published_status(self, request, pk=None):
        post = Post.objects.get(pk=pk)
        if request.method == 'GET':
            serializer = FeaturedAndPublishedSerializer(post)
            return Response(serializer.data)
        else:
            serializer = FeaturedAndPublishedSerializer(data=request.data,partial=True)
            if serializer.is_valid():
                post.published = serializer.validated_data['published']
                post.featured  = serializer.validated_data['featured']
                post.save()
                return Response(
                    {'status':'Updated'},
                    status=204
                )
            else: 
                return Response(serializer.errors,status=400)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    lookup_field = 'pk'
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]