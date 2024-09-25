from rest_framework import serializers
from .models import Post, Comment
from django.contrib.auth import get_user_model


class PostSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source="author.username", read_only=True)

    class Meta:
        model = Post
        fields = ["id", "author", "title", "like"]
        # fields = ["username", "author", "title", "like"]


class PostDetailSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source="author.username", read_only=True)
    commets_count = serializers.IntegerField(source="comments.count", read_only=True)

    class Meta:
        model = Post
        fields = "__all__"
        read_only_fields = ["author"]


class CommentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["author", "content", "created_at"]


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["content"]
