from django.urls import path
from . import views

urlpatterns = [
    path("<int:post_pk>/comment/", views.CommentLIstCreateView.as_view()),
    path(
        "comment/<int:pk>",
        views.CommentUpdateDeleteView.as_view(),
    ),
]
