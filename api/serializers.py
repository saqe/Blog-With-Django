from blog.models import Post
from django.contrib.auth.models import User
from rest_framework import serializers

from users.models import Profile
from blog.models import PostTag

class BlogSerializer(serializers.ModelSerializer):
    tags = serializers.SlugRelatedField(
        queryset=PostTag.objects.all(),
        many=True,
        slug_field='tag',)
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',)
    slug = serializers.SlugField(read_only=True)
    class Meta:
        model = Post
        fields = (
            'url',
            'title',
            'slug',
            'posted_datetime',
            'updated_datetime',
            'content',
            'author',
            'tags',
        )

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)

    def create(self, validated_data):
        validated_data['author'] = self.context.get('request').user
        return super().create(validated_data)

class FeaturedAndPublishedSerializer(serializers.ModelSerializer):
    title=serializers.CharField(read_only=True)
    slug=serializers.SlugField(read_only=True)
    class Meta:
        model = Post
        fields= (
            'id',
            'title',
            'slug',
            'published',
            'featured')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields=(
            "id",
            'url',
            "is_active",
            "username",
            "first_name",
            "last_name",
            "email",
            "is_staff",
            "is_superuser",
            "last_login",
            "date_joined",
        )

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields=(
            "__all__"
        )
