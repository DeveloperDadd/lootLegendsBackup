from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
from rest_framework import routers
from lootlegends import views
from lootlegends.views import *


router = routers.DefaultRouter()
router.register(r'game', GameViewSet)
router.register(r'media', MediaViewSet)
router.register(r'genre', GenreViewSet)
router.register(r'post', PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('user/signup/', UserCreate.as_view(), name="create_user"),
    path('users/<int:pk>/', UserDetail.as_view(), name="get_user_details"),
    path('user/login/', jwt_views.TokenObtainPairView.as_view(), name='token_create'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('add-to-favorites/', views.add_favorite_game, name="add-to-favorites"),
]