from django.urls import path
from .views import CrawlerHealthChosun, ArticleSummarizer

urlpatterns = [
    path('Chosun/', CrawlerHealthChosun.as_view()),
    path('summarize/', ArticleSummarizer.as_view()),
]
