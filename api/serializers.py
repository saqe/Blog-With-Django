from blog.models import Post
from rest_framework import serializers

class BlogSerializer(serializers.ModelSerializer):
    tags = serializers.SlugRelatedField(many=True,read_only=True,slug_field='tag')
    author = serializers.SlugRelatedField(read_only=True,slug_field='email')
    is_published = serializers.BooleanField(read_only=True)
    class Meta:
        model = Post
        fields = ('url','title','posted_datetime','updated_datetime','content','author','tags','is_published')
