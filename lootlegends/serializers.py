from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from .models import *

class CustomUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True
    )
    username = serializers.CharField()
    password = serializers.CharField(min_length=8, write_only=True)
    
    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'password', 'first_name', 'last_name')
        extra_kwargs = {'password': {'write_only': True}}
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model: Media
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model: Post
        fields ='__all__'

class GenreSerializers(serializers.ModelSerializer):
    class Meta:
        model: Genre
        fields = '__all__'

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model: Game
        fields = '__all__'

