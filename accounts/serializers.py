from .models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
        )


class UserProfileSerializer(serializers.ModelSerializer):

    # username = serializers.CharField(source='user.username', read_only=True)  # User 모델의 username, email 필드 가져오기
    # email = serializers.EmailField(source='user.email', read_only=True) 

    class Meta:
        model = User
        fields = ['profile_image', "username", "email"]  # 반환 및 수정할 필드 목록
