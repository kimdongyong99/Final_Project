from rest_framework import serializers
from .models import Post, Comment
from django.contrib.auth import get_user_model


class PostSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source="author.username", read_only=True)

    class Meta:
        model = Post
        fields = ["id", "author", "title", "likes_count", "image"]


class PostDetailSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source="author.username", read_only=True)
    commets_count = serializers.IntegerField(source="comments.count", read_only=True)
    likes_count = serializers.SerializerMethodField() # 이걸 지정하지 않으면 좋아요가 상세에선 계속 0으로 표시됨

    def get_likes_count(self, obj):
        return obj.likes.count()

    class Meta:
        model = Post
        fields = "__all__"
        read_only_fields = ["author"]

class PostLikeSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    likes = serializers.StringRelatedField(many=True)
    likes_count = serializers.SerializerMethodField()

    def get_user(self, obj):
        return obj.user.username

    def get_likes_count(self, obj):
        return obj.likes.count()

    class Meta:
        model = Post
        fields = ("id", "author", "user", "likes_count", 'likes')


class CommentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["author", "content", "created_at"]


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["content"]
