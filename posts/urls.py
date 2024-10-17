from django.urls import path
from . import views

urlpatterns = [
    path("", views.PostListView.as_view(), name="post"),
    path("<int:post_pk>/", views.PostDetailView.as_view()),
    path("<int:post_pk>/comment/", views.CommentLIstCreateView.as_view()),
    path("comment/<int:pk>", views.CommentUpdateDeleteView.as_view()),
    path("<int:post_pk>/like/", views.PostLikeView.as_view()),
    path("<int:hash_pk>/hash/", views.PostHashtagView.as_view()),
    # 유저가 좋아요한 게시글 목록 가져오기
    path("<str:username>/liked_posts/", views.LikedPostsView.as_view()),
]
