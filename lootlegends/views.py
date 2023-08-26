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
    user = request.user #Getting user id sent from the frontend and setting it equal to user
    rawg_id = request.data.get("rawg_id") #Getting the rawg_id sent from the 3rd party API and setting it equal to rawg_id
    game_data = request.data

    game = Game.objects.filter(rawg_id__exact=rawg_id)
    if not game:
        game_serializer = GameSerializer(data=game_data)
        if game_serializer.is_valid():
            game_instance = game_serializer.save()
            game = game_instance.

    userfavorite

    try:
        game = Game.objects.filter(rawg_id=rawg_id) #Checking to see if the Game model has a matching record where rawg_id equals the rawg_id from the frontend
    except Game.DoesNotExist: # If the game doesn't exist do the below:
        game = Game.objects.create(request.data) #Create a new record in the Game model equal to the data sent from the frontend
        game.save() #save it to the Game model 

    try:
        user_favorite_game = UserFavoriteGames.objects.filter(game=rawg_id).first() #Filter the UserFavoriteGames by user id and the rawg id
        user_favorite_game.delete() # If there's a match delete it from the UserFavoriteGames model
        message = 'Game removed from favorites' #Message sent after successful deletion
        response_status = status.HTTP_200_OK #response status sent back
    except UserFavoriteGames.DoesNotExist:
        user_favorite_game = UserFavoriteGames.objects.create(user=user, game=rawg_id) #If the record does not exist, add it to the UserFavoriteGames table
        user_favorite_game.save() #Save it to UserFavoriteGame model for future use
        message = 'Game added to favorites' #message sent back after added successfully to favorites
        response_status = status.HTTP_201_CREATED #response sent back if added to favorites
    return Response({'message':message}, status=response_status) #See the conditions above
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def favorite_games_for_user(request):
    user = request.user
    favorite_games = UserFavoriteGames.objects.filter(user=user)
    serializer = UserFavoriteGamesSerializer(favorite_games, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
