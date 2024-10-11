from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Article(models.Model):
    title = models.CharField(max_length=300)
    link = models.URLField(max_length=500)
    image_url = models.URLField(max_length=500, null=True, blank=True)
    summary = models.TextField(null=True, blank=True)
    likes = models.ManyToManyField(User, related_name='liked_articles', blank=True)  # ManyToManyField로 유저의 좋아요 추가

    def __str__(self):
        return self.title

    def total_likes(self):
        return self.likes.count()
    
