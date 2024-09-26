from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import timedelta
from django.utils import timezone

# Create your models here.


class User(AbstractUser):
    created_at = models.DateTimeField(auto_now_add=True)
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    
    def __str__(self):
        return self.username

      
class EmailVerification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # 인증번호와 유저 연결
    code = models.CharField(max_length=6)  # 6자리 인증번호
    created_at = models.DateTimeField(auto_now_add=True)  # 생성 시간 자동 저장

    # 인증번호가 유효한지 확인 (10분 유효)
    def is_valid(self):
        return self.created_at + timedelta(minutes=10) > timezone.now()


class UserProfile(models.Model):
    # User 모델과 1:1 관계 설정
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)  # 프로필 사진

    def __str__(self):
        return self.user.username  # 사용자 이름 반환
