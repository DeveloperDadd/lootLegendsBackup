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
def favorite_game(request, game_id):
    user = request.user
    game = get_object_or_404(Game, id=game_id)

    if request.method == 'POST':
        if UserFavoriteGames.objects.filter(user=user, game=game).exists():
            return Response({'message':'Game is already in favorites'}, status=status.HTTP_400_BAD_REQUEST)
    
        favorite = UserFavoriteGames(user=user, game=game)
        favorite.save()
        return Response({'message': 'Game added to favorites'}, status=status.HTTP_201_CREATED)
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def favorite_games_for_user(request):
    user = request.user
    favorite_games = UserFavoriteGames.objects.filter(user=user)
    serializer = UserFavoriteGamesSerializer(favorite_games, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
