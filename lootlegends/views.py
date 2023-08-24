from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status, permissions, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action
from .models import *
from .serializers import * 
from django.db.models import Sum
from rest_framework.decorators import api_view


class UserCreate(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()
    def post(self, request, format='json'):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetail(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all();
    serializer_class = CustomUserSerializer;

class MediaViewSet(viewsets.ModelViewSet):
    queryset = Media.objects.all();
    serializer_class = MediaSerializer;

class PostViewSet(viewsets.ModelViewSet):
    queryset = Media.objects.all();
    serializer_class = PostSerializer;

class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all();
    serializer_class = GenreSerializer;

class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all();
    serializer_class = GameSerializer;