from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User, EmailVerification
from .validators import validate_signup
from .serializers import UserSerializer, UserProfileSerializer
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.exceptions import TokenError
from .utils import generate_verification_code, send_verification_email
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


class SignupView(APIView):
    def post(self, request):
        # 유효성 검사
        is_valid, err_msg = validate_signup(request.data)
        if not is_valid:
            return Response({"error": err_msg}, status=400)

        # 비밀번호와 비밀번호 확인
        password = request.data.get("password")
        password_confirm = request.data.get("password_confirm")

        if password != password_confirm:
            return Response({"error": "비밀번호가 일치하지 않습니다."}, status=400)

        # 회원 정보 입력받기
        username = request.data.get("username")
        email = request.data.get("email")
        profile_image = request.FILES.get("profile_image")

        # 유저 생성
        user = User.objects.create_user(
            username=username,
            password=password,
            email=email,
            profile_image=profile_image
        )

        # 유저 직렬화 및 응답
        serializer = UserSerializer(user)
        return Response(serializer.data)


class LoginView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if not user:
            return Response(
                {"error": "아이디 혹은 비밀번호가 올바르지 않습니다."}, status=400
            )
        
        serializer = UserSerializer(user)
        res_data = serializer.data
        refresh = RefreshToken.for_user(user)
        res_data["access_token"] = str(refresh.access_token)
        res_data["refresh_token"] = str(refresh)
        return Response(res_data)


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        refresh_token_str = request.data.get("refresh_token")
        try:
            refresh_token = RefreshToken(refresh_token_str)
        except TokenError as e:
            return Response({"msg": str(e)}, status=400)
        
        refresh_token.blacklist()
        return Response(status=200)


class RequestEmailVerificationView(APIView):
    def post(self, request):
        email = request.data.get("email")
        user = User.objects.filter(email=email).first()

        if not user:
            return Response({"error": "해당 이메일로 등록된 유저가 없습니다."}, status=400)

        # 인증번호 생성 및 이메일로 전송
        code = generate_verification_code()
        send_verification_email(user.email, code)

        # 인증번호 저장
        EmailVerification.objects.create(user=user, code=code)
        return Response({"message": "인증번호가 이메일로 발송되었습니다."}, status=200)


class VerifyEmailView(APIView):
    def post(self, request):
        email = request.data.get("email")
        code = request.data.get("code")
        user = User.objects.filter(email=email).first()

        if not user:
            return Response({"error": "유저를 찾을 수 없습니다."}, status=400)

        # 인증번호 검증
        verification = EmailVerification.objects.filter(user=user, code=code).first()

        if verification and verification.is_valid():
            verification.delete()  # 인증 완료 후 인증번호 삭제
            return Response({"message": "이메일 인증이 완료되었습니다."}, status=200)
        else:
            return Response({"error": "잘못된 인증번호이거나 유효시간이 지났습니다."}, status=400)


class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]  # 인증된 사용자만 접근 가능

    def get(self, request, username):
        # 사용자 이름으로 User 객체 조회
        user = get_object_or_404(User, username=username)
        serializer = UserProfileSerializer(user) 
        return Response(serializer.data)  # 직렬화된 데이터 반환

    def put(self, request, username):
        # 사용자 이름으로 User 객체 조회
        user = get_object_or_404(User, username=username)

        # 현재 사용자와 요청한 사용자가 동일한지 확인
        if user != request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)  # 권한 없음 응답

        serializer = UserProfileSerializer(user, data=request.data, partial=True)  # 데이터로 시리얼라이저 초기화
        if serializer.is_valid():  # 유효성 검사
            serializer.save()  # 시리얼라이저를 통해 프로필 정보 저장
            return Response({'message': '프로필이 업데이트 되었습니다.'}, status=status.HTTP_200_OK)  # 성공 메시지 반환

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # 오류 반환
