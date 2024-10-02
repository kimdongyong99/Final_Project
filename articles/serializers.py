from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    total_likes = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = ['id', 'title', 'link', 'image_url', 'total_likes']

    def get_total_likes(self, obj):
        return obj.total_likes()
