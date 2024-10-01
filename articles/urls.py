from django.urls import path
from .views import CrawlerNewsList, CrawlerHealthChosun

urlpatterns = [
    path('news/', CrawlerNewsList.as_view(), name='news_list'),
    path('Chosun/', CrawlerHealthChosun.as_view(), name='news_list'),
]
