from rest_framework import serializers
from .models import Post, Comment
from django.contrib.auth import get_user_model


class PostSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source="users.username", read_only=True)

    class Meta:
        model = Post
        fields = ["username", "author", "title", "like"]


class CommentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["author", "content", "created_at"]


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["content"]
