from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User
from .validators import validate_signup
from .serializers import UserSerializer

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