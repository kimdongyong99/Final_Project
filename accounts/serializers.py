from .models import User
from rest_framework import serializers
from articles.serializers import ArticleSerializer
from posts.serializers import PostSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "email",
            "address",
            "profile_image"
        )



class UserProfileSerializer(serializers.ModelSerializer):

    username = serializers.CharField(read_only=True)  # User 모델의 username, email 필드 가져오기
    email = serializers.EmailField(read_only=True) 
    liked_articles = ArticleSerializer(many=True, read_only=True)
    post = PostSerializer(many=True, read_only=True) # 내가 작성한 게시글
    like_post = PostSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['profile_image', "username", "email","address","detail_address", "liked_articles", "post", "like_post"]  # 반환 및 수정할 필드 목록