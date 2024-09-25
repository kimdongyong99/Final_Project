from django.shortcuts import render
from rest_framework import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from .models import Post


class PostListView(ListAPIView):
    pass