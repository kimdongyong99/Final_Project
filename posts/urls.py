from django.urls import path
from . import views

urlpatterns = [
    path("", views.PostListView.as_view(), name="post"),
    path("<int:pk>/", views.PostDetailView.as_view()),
    path("<int:post_pk>/comment/", views.CommentLIstCreateView.as_view()),
    path(
        "comment/<int:pk>",
        views.CommentUpdateDeleteView.as_view(),
    ),
]
