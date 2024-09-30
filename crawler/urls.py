from django.urls import path
from .views import CrawlerNewsList, CrawlerHealthChosun
# from .views import ArticleSummarizer

urlpatterns = [
    path('news/', CrawlerNewsList.as_view(), name='news_list'),
    path('Chosun/', CrawlerHealthChosun.as_view(), name='news_list'),
    # path('summarize/', ArticleSummarizer.as_view(), name='summarize'),
]
