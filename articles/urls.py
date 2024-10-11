from django.urls import path
from .views import CrawlerNewsList, ArticleSummarizer, ArticleDetailAPIView, ArticleLikeView

urlpatterns = [
    path('news/', CrawlerNewsList.as_view()),
    path('summarize/', ArticleSummarizer.as_view()),
    path('<int:pk>/', ArticleDetailAPIView.as_view()),
    path('<int:article_id>/like/', ArticleLikeView.as_view()),
]
