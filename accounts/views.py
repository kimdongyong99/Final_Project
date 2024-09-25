from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User
from .validators import validate_signup
from .serializers import UserSerializer
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.
class SignupView(APIView):
    def post(self, request):
        is_valid, err_msg = validate_signup(request.data)
        if not is_valid:
            return Response({"error": err_msg}, status=400)

        username = request.data.get("username")
        password = request.data.get("password")
        email = request.data.get("email")
        profile_image = request.FILES.get("profile_image")

        user = User.objects.create_user(
            username=username,
            password=password,
            email=email,
            profile_image=profile_image
        )

        serializer = UserSerializer(user)
        return Response(serializer.data)


class SigninView(APIView):
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