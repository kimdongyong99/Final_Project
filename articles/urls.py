from django.urls import path
from .views import CrawlerNewsList, ArticleSummarizer, ArticleDetailAPIView, ArticleLikeView, CommentListCreateView, CommentUpdateDeleteView,LikedArticlesView

urlpatterns = [
    path('news/', CrawlerNewsList.as_view()),
    path('summarize/', ArticleSummarizer.as_view()),
    path('<int:pk>/', ArticleDetailAPIView.as_view()),
    path('<int:article_id>/like/', ArticleLikeView.as_view()),
    path('<int:article_pk>/comments/', CommentListCreateView.as_view()),  # 댓글 조회 및 작성
    path('comments/<int:pk>/', CommentUpdateDeleteView.as_view()),  # 댓글 수정 및 삭제
    path('<str:username>/liked_articles/', LikedArticlesView.as_view()),  # 사용자 좋아요한 기사 목록 조회
]
