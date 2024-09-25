from rest_framework import serializers
from .models import Post
from django.contrib.auth import get_user_model

class PostSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source="users.username", read_only=True)

    class Meta:
        model = Post
        fields = ["username", "author", "title", "like"]