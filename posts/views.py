from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly # 아직 settings에서 권한설정 안함
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from django.db.models import Q
from .models import Post, Comment
from django.shortcuts import get_object_or_404
from rest_framework.generics import(
ListAPIView,
ListCreateAPIView,
UpdateAPIView,
DestroyAPIView)
from .serializers import(
PostSerializer,
PostDetailSerializer,
CommentListSerializer,
CommentCreateSerializer)


class PostListView(APIView):
    # permission_classes = [IsAuthenticatedOrReadOnly]
    pagenation_class = PageNumberPagination # pagination 작업.
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
    # 글 조회
    def get(self, request):
        products = Post.objects.all()
        serializer = PostSerializer(products, many=True)
        return Response(serializer.data)
    
    

class PostDetailView(APIView):
    # permission_classes = [IsAuthenticatedOrReadOnly]
    # 글 상세
    def get(self, request, pk):
        products = get_object_or_404(Post, pk=pk)
        serializer = PostDetailSerializer(products)
        return Response(serializer.data)
    # 글 수정
    def put(self, request, pk):
        products = get_object_or_404(Post, pk=pk)
    # 예외 처리
        if products.author != request.user: # 작성자 본인이 아닌 상태
            return Response(
                data={"detail": "본인의 작성글만 수정할 수 있습니다."},
                status=status.HTTP_403_FORBIDDEN, # 본인의 글이 아니므로 금지된 접근 처리
            )

        serializer = PostDetailSerializer(products, data=request.data, partial=True)
        if serializer.is_valid():
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        products = get_object_or_404(Post, pk=pk)
        # 다른 사람이 삭제하면 안되니까 예외처리
        if products.author != request.user:
            return Response(
                data={"detail": "본인의 게시글만 삭제할 수 있습니다."},
                status=status.HTTP_403_FORBIDDEN # 다른 사람이 삭제 시도 시 금지된 접근 처리
            )
        products.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



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
