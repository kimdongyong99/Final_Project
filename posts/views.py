from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    UpdateAPIView,
    DestroyAPIView,
)
from .models import Post
from .serializers import CommentListSerializer, CommentCreateSerializer
from .models import Comment
from django.shortcuts import get_object_or_404


class PostListView(ListAPIView):
    pass


class CommentLIstCreateView(ListCreateAPIView):

    def get_queryset(self):
        post_id = self.kwargs["post_pk"]  # URL에서 post_pk 가져오기
        return Comment.objects.filter(
            post_id=post_id
        )  # 특정 포스트에 대한 댓글만 가져옴

    def get_serializer_class(self):
        if self.request.method == "GET":
            return CommentListSerializer
        return CommentCreateSerializer


class CommentUpdateDeleteView(UpdateAPIView, DestroyAPIView):
    queryset = Comment.objects.all()
    lookup_field = "pk"

    def get_serializer_class(self):
        if self.request.method == "PUT":
            return CommentCreateSerializer
