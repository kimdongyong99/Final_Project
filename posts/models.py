from django.db import models
from django.conf import settings


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
    like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_post", blank=True)

    def __str__(self):
        return self.title