from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class CustomUser(AbstractUser):

    def __str__(self):
        return self.username
    
class User(models.Model):
    username = models.CharField(max_length=16)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=16)
    date_registered = models.DateTimeField()

class Media(models.Model):
    user_id = models.ManyToManyField(
        User,
        through="PostMedia"
    )
    type = models.IntegerField()
    asset_url = models.CharField()
    date_uploaded = models.DateTimeField()

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post_text = models.CharField(max_length=140)
    date_posted = models.DateTimeField()

class PostMedia(models.Model):
    media = models.ForeignKey(Media, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

class Genre(models.Model):
    genre_type = models.CharField(max_length=100)

class Game(models.Model):
    game_title = models.CharField(max_length=255)
    rawg_id = models.IntegerField()
    user = models.ManyToManyField(
        User,
        through="UserFavoriteGames"
    )
    game_cover_art = models.CharField()
    posts = models.ManyToManyField(
        Post,
        through="GamePost"
    )
    genre = models.ManyToManyField(
        Genre,
        through="GameGenre"
    )

class UserFavoriteGames(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

class GameGenre(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

class GamePost(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class ProfilePicture(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    media_id = models.ForeignKey(Media, on_delete=models.CASCADE)



    