from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)  # 아직 settings에서 권한설정 안함
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView
from rest_framework.pagination import PageNumberPagination
from django.db.models import Q
from .models import Post, Comment, Hashtag
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    UpdateAPIView,
    DestroyAPIView,
    GenericAPIView,
)
from .serializers import (
    PostSerializer,
    PostDetailSerializer,
    PostLikeSerializer,
    HashtagSerializer,
    CommentListSerializer,
    CommentCreateSerializer,
)
from rest_framework.parsers import MultiPartParser, FormParser


class PostListView(ListAPIView):
    # List APIView에 이미 get이 들어가 있어서 밑에 get을 쓰지 않고도 Post.objects.all만 주고도 전체 조회가 가능함.
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagenation_class = PageNumberPagination  # pagination 작업.
    serializer_class = PostSerializer

    def get_queryset(
        self,
    ):  # ListAPIView 사용시, post.objects.all()만으로 전체 조회 가능
        search = self.request.query_params.get("search")
        order_by = self.request.query_params.get("order_by")
        queryset = Post.objects.all()

        # 검색 기능(ListAPIView 상속시 사용가능)
        if search:
            return Post.objects.filter(
                Q(title__icontains=search) |
                Q(content__icontains=search) |
                Q(hashtags__hashtag__icontains=search) |
                Q(author__username__icontains=search)
            ).distinct()
        if order_by == "likes":
            queryset = queryset.order_by("-likes_count")
        else:  # 기본값은 최신순
            queryset = queryset.order_by("-created_at")

        return queryset

    def post(self, request):  # 게시글 작성
        title = request.data.get("title")
        content = request.data.get("content")
        image = request.data.get("image")  # 22 ~ 24줄까지 데이터 추출
        hashtags_data = request.data.get("hashtags", "")
        # 예외처리
        if not title:
            return Response(
                data={"message": "제목을 입력하세요."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        if not content:
            return Response(
                data={"message": "내용을 입력하세요."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        product = Post.objects.create(
            title=title,
            content=content,
            image=image,
            author=request.user,  # 해시태그는 manytomanyfield이므로 직접 지정 금지.(지정시 오류 발생)
        )
        # 해시태그를 하나의 문자열로 처리
        if hashtags_data:
            hashtag_names = hashtags_data.split(",")  # 쉼표로 구분하여 해시태그 리스트 생성
            for hashtag_name in hashtag_names:
                hashtag_name = hashtag_name.strip()  # 공백 제거
                if hashtag_name:  # 빈 문자열 체크
                    # 해시태그 앞에 # 추가
                    hashtag_name_with_hash = f"#{hashtag_name}"
                    hashtag, created = Hashtag.objects.get_or_create(
                        hashtag=hashtag_name_with_hash
                    )  # 해시태그 생성 또는 조회
                    product.hashtags.add(hashtag)

        return Response({"id": product.id}, status=status.HTTP_201_CREATED)


class PostHashtagView(ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()  # queryset을 정의

    def get(self, request, hash_pk):
        post = get_object_or_404(Post, pk=hash_pk)
        serializer = self.get_serializer(post)
        return Response(serializer.data)

    def post(self, request, hash_pk):
        post = get_object_or_404(Post, pk=hash_pk)
        hashtags_data = request.data.get("hashtags", [])

        for hashtag_name in hashtags_data:
            hashtag, created = Hashtag.objects.get_or_create(name=hashtag_name)
            post.hashtags.add(hashtag)

        post.save()
        return Response(
            {"message": "해시태그 등록을 성공하였습니다."},
            status=status.HTTP_201_CREATED,
        )


class PostDetailView(APIView):
    parser_classes = [MultiPartParser, FormParser]  # 멀티파트와 폼 데이터를 처리하기 위한 파서 추가

    # 글 상세
    def get(self, request, post_pk):
        products = get_object_or_404(Post, pk=post_pk)
        serializer = PostDetailSerializer(products)
        return Response(serializer.data)

    # 글 수정
    def put(self, request, post_pk):
        products = get_object_or_404(Post, pk=post_pk)
        
        # 작성자 확인
        if products.author != request.user:
            return Response(
                {"detail": "본인의 작성글만 수정할 수 있습니다."},
                status=status.HTTP_403_FORBIDDEN,
            )

        # 해시태그 데이터 처리
        hashtags_data = request.data.get("hashtags", "")

        # 게시글 업데이트
        serializer = PostDetailSerializer(products, data=request.data, partial=True)
        if serializer.is_valid():
            post = serializer.save()  # 게시글 저장

            # 기존 해시태그 삭제
            post.hashtags.clear()

            # 해시태그 처리
            if hashtags_data:
                # 해시태그가 리스트 또는 문자열일 경우 처리
                if isinstance(hashtags_data, str):
                    hashtag_names = hashtags_data.split(",")
                elif isinstance(hashtags_data, list):
                    hashtag_names = hashtags_data
                else:
                    hashtag_names = []

                for hashtag_name in hashtag_names:
                    hashtag_name = hashtag_name.strip()  # 공백 제거
                    if hashtag_name:
                        # 해시태그 앞에 #이 없으면 추가
                        if not hashtag_name.startswith("#"):
                            hashtag_name = f"#{hashtag_name}"
                        hashtag, created = Hashtag.objects.get_or_create(
                            hashtag=hashtag_name
                        )
                        post.hashtags.add(hashtag)

            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 글 삭제
    def delete(self, request, post_pk):
        products = get_object_or_404(Post, pk=post_pk)
        if products.author != request.user:
            return Response(
                {"detail": "본인의 게시글만 삭제할 수 있습니다."},
                status=status.HTTP_403_FORBIDDEN,
            )
        products.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PostLikeView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    # 좋아요 기능
    def post(self, request, post_pk):
        post = get_object_or_404(Post, pk=post_pk)  # post_pk값을 가져옴
        user = request.user
        if user in post.likes.all():  # 좋아요 한 유저를 조회해서 이미 좋아요를 누른 유저가 누를 경우
            post.likes.remove(user)
            post.likes_count -= 1
            post.save()
            return Response({
                "message": "좋아요 취소",
                "likes_count": post.likes.count()  # 실시간으로 좋아요 수 반환
            }, status=status.HTTP_200_OK)
        else:
            post.likes.add(user)
            post.likes_count += 1
            post.save()
            return Response({
                "message": "좋아요",
                "likes_count": post.likes.count()  # 실시간으로 좋아요 수 반환
            }, status=status.HTTP_200_OK)


# 좋아요한 게시글 목록
User = get_user_model()

class LikedPostsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, username):
        user = User.objects.get(username=username)
        liked_posts = user.like_post.all()  # User 모델에서 역참조하여 좋아요한 게시글 가져오기
        serializer = PostSerializer(liked_posts, many=True)
        return Response({'results': serializer.data}, status=200)


class CommentLIstCreateView(ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = PageNumberPagination
    
    def get_queryset(self):
        post_id = self.kwargs["post_pk"]
        return Comment.objects.filter(post_id=post_id)

    def get_serializer_class(self):
        if self.request.method == "GET":
            return CommentListSerializer
        return CommentCreateSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({
            'post_pk': self.kwargs['post_pk'],
        })
        return context


class CommentUpdateDeleteView(UpdateAPIView, DestroyAPIView):
    queryset = Comment.objects.all()
    lookup_field = "pk"

    def get_serializer_class(self):
        if self.request.method == "PUT":
            return CommentCreateSerializer
