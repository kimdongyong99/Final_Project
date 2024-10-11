from django.db import models
from django.conf import settings


class Hashtag(models.Model):
    hashtag = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.hashtag


class Post(models.Model):
    author = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="post",
    )
    title = models.CharField(max_length=30)
    content = models.TextField()
    image = models.ImageField(upload_to="posts/image/", null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="like_post", blank=True
    )
    likes_count = models.PositiveIntegerField(default=0)
    hashtags = models.ManyToManyField(
        Hashtag, blank=True, related_name="posts_hashtags"
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-id"]  # 저장할 때 역순으로 정렬해준다.


class Comment(models.Model):
    author = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="comment",
        null=True,
        blank=True,
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="post_comment",
        null=True,
        blank=True,
    )
    content = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
