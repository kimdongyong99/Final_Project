from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly # 아직 settings에서 권한설정 안함
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView
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
PostLikeSerializer,
CommentListSerializer,
CommentCreateSerializer)


class PostListView(ListAPIView):
    # List APIView에 이미 get이 들어가 있어서 밑에 get을 쓰지 않고도 Post.objects.all만 주고도 전체 조회가 가능함.
    # permission_classes = [IsAuthenticatedOrReadOnly]
    pagenation_class = PageNumberPagination # pagination 작업.
    serializer_class = PostSerializer

    def get_queryset(self): # ListAPIView 사용시, post.objects.all()만으로 전체 조회 가능
        search = self.request.query_params.get("search") # 검색 기능(ListAPIView 상속시 사용가능)
        if search:
            return Post.objects.filter(
                Q(title__icontains=search) | Q(content__icontains=search) # 필터링을 위해 Q 객체로 검색 조건 지정
            )
        return Post.objects.all() # 게시글 전체 조회(ListAPIView를 받아 사용하기에 get 코드를 쓰지 않아도 해결가능)
    

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
#     # 글 조회
#     # def get(self, request):
#     #     products = Post.objects.all()
#     #     serializer = PostSerializer(products, many=True)
#     #     return Response(serializer.data)
    


class PostDetailView(APIView):
    # permission_classes = [IsAuthenticatedOrReadOnly]
    # 글 상세
    def get(self, request, post_pk):
        products = get_object_or_404(Post, pk=post_pk)
        serializer = PostDetailSerializer(products)
        return Response(serializer.data)
    # 글 수정
    def put(self, request, post_pk):
        products = get_object_or_404(Post, pk=post_pk)
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
    


class PostLikeView(APIView):
    # permission_classes = [IsAuthenticatedOrReadOnly]

    # 좋아요만 조회
    def get(self, request, post_pk):
        post = get_object_or_404(Post, pk=post_pk)
        serializer = PostLikeSerializer(post)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 좋아요 기능
    def post(self, request, post_pk):
        post = get_object_or_404(Post, pk=post_pk)# post_pk값을 가져옴
        if request.user in post.likes.all(): # 좋아요 한 유저를 조회해서 이미 좋아요를 누른 유저가 누를 경우
            post.likes.remove(request.user)
            return Response("좋아요 취소", status=status.HTTP_204_NO_CONTENT)
        else:
            post.likes.add(request.user)
            return Response("좋아요", status=status.HTTP_201_CREATED) # 좋아요를 누르지 않았다면 좋아요를 누른 상태가 된다.
    # def post(self, request, post_pk):
    #     post = Post.objects.get(pk=post_pk)
    #     author = request.user

    #     if author in post.like.all():
    #         post.like.remove(author)
    #         return Response({"message : 좋아요 취소"}, status=status.HTTP_204_NO_CONTENT)
    #     post.like.add(author)
    #     return Response({"message": "좋아요"}, status=status.HTTP_201_CREATED)




class CommentLIstCreateView(ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
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
