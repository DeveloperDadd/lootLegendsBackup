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
   try:
        user = request.user
        game_id = request.data.get('rawg_id')

        existing_favorite=UserFavoriteGames.objects.filter(user=user, game_id=game_id).first()

        if existing_favorite:
            return Response({'detail':'Game already in favorites.'}, status=status.HTTP_400_BAD_REQUEST)

        game = Game.objects.get(pk=rawg_id)
        user_favorite_game = UserFavoriteGames(user=user, game=game)
        user_favorite_game.save()

        return Response({'detail':'Game added to favorites'}, status=status.HTTP_201_CREATED)
   except Exception as e:
        return Response({'detail':str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
   
    # user = request.user
    # games = Game.objects.all()
    # serializer = UserFavoriteGamesSerializer(games, many=True)
    # return Response(serializer.data)

    # if Game.objects.filter(rawg_id=game):
    #     UserFavoriteGames.objects.create(game=game, user=user)
    #     return Response({'message':'Game added to favorites'})
    # elif Game.objects.filter(id != game):
    #     Game.objects.create(request.data)
    #     UserFavoriteGames.objects.create(game=game, user=user)
    # elif UserFavoriteGames.objects.filter(game=game):
    #     UserFavoriteGames.objects.delete(game=game)
    #     return Response({'message': 'Game was unfavorited'})
    
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def favorite_games_for_user(request):
    user = request.user
    favorite_games = UserFavoriteGames.objects.filter(user=user)
    serializer = UserFavoriteGamesSerializer(favorite_games, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
