from rest_framework import serializers
from .models import Article, Comment

class ArticleSerializer(serializers.ModelSerializer):
    total_likes = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = ['id', 'title', 'link', 'image_url', 'total_likes']

    def get_total_likes(self, obj):
        return obj.total_likes()


class CommentListSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    author_id = serializers.PrimaryKeyRelatedField(source='author.id', read_only=True)  # author_id 필드를 추가

    class Meta:
        model = Comment
        fields = ['id', 'author', 'author_id', 'content', 'created_at']  # author_id를 fields에 추가


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['content']