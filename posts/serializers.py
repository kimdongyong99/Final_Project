from rest_framework import serializers
from .models import Post
from django.contrib.auth import get_user_model

class PostSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source="author.username", read_only=True)

    class Meta:
        model = Post
        fields = ["id", "author", "title", "like"]