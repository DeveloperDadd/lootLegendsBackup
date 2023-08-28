from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status, permissions, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action, api_view, permission_classes
from .models import *
from .serializers import * 
from django.db.models import Sum
from rest_framework.decorators import api_view
from corsheaders.middleware import CorsMiddleware
from django.views.decorators.http import require_POST
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
import json

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
    queryset = CustomUser.objects.all();
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


@api_view(['POST'])
def add_favorite_game(request):
    if request.method == 'POST':
        user=request.data.get("user_id")
        rawg_id = request.data.get("rawg_id")
        game_data = request.data
        game_id = 0

        game = Game.objects.filter(rawg_id__exact=rawg_id)
        if not game:
            game_serializer = GameSerializer(data=game_data)
            if game_serializer.is_valid():
                game_instance = game_serializer.save()
                game_id = game_instance.id
        else:
            game_id = game.first().id

        favorite_game_data = {
            'user': user,
            'game': game_id,
        }

        favorites = UserFavoriteGames.objects.filter(game=game_id, user=user)
        if not favorites:
            user_favorite_games_serializer = UserFavoriteGamesSerializer(data=favorite_game_data)
            if user_favorite_games_serializer.is_valid():
                user_favorite_games_serializer.save()
                return Response({'message': 'Game added to favorites'}, status=status.HTTP_201_CREATED)
            return Response(user_favorite_games_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message': 'Game already in favorites'}, status=status.HTTP_200_OK)
    return Response({'message': 'Invalid request method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def favorite_games_for_user(request):
    user = request.user
    favorite_games = UserFavoriteGames.objects.filter(user=user)
    serializer = UserFavoriteGamesSerializer(favorite_games, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

