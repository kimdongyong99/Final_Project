from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=300)
    link = models.URLField(max_length=500)
    image_url = models.URLField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.title