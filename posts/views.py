from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated # 아직 settings에서 권한설정 안함
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
# from rest_framework.pagination import PageNumberPagination
from django.db.models import Q
from .models import Post
from .serializers import PostSerializer


class PostListView(APIView):
    # pagenation_class = PageNumberPagination
    def get_queryset(self):
        search = self.request.query_params.get("search")
        if search:
            return Post.objects.filter(
                Q(title__icontains=search) | Q(content__icontains=search) # 필터링을 위해 Q 객체로 검색 조건 지정
            )
        return Post.objects.all()

    def post(self, request): # 게시글 작성
        title = request.data.get("title")
        content = request.data.get("content")
        image = request.data.get("image") # 22 ~ 24줄까지 데이터 추출
            # 예외처리
        if not title:
            return Response(
                data={"message":"제목을 입력하세요."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        if not content:
            return Response(
                data={"message":"내용을 입력하세요."},
                status=status.HTTP_400_BAD_REQUEST
            )
        product = Post.objects.create(
            title = title,
            content=content,
            image=image,
            author=request.user,
        )
        serializer = PostSerializer(product)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def get(self, request):
        products = Post.objects.all()
        serializer = PostSerializer(products, many=True)
        return Response(serializer.data)

