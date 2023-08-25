from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class CustomUser(AbstractUser):

    def __str__(self):
        return self.username

class Media(models.Model):
    user_id = models.ManyToManyField(
        CustomUser,
        through="PostMedia"
    )
    type = models.IntegerField()
    asset_url = models.CharField()
    date_uploaded = models.DateTimeField()

class Post(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post_text = models.CharField(max_length=140)
    date_posted = models.DateTimeField()

class PostMedia(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.PROTECT)
    media = models.ForeignKey(Media, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

class Genre(models.Model):
    genre_type = models.CharField(max_length=100)

class Game(models.Model):
    game_title = models.CharField(max_length=255)
    rawg_id = models.IntegerField()
    user = models.ManyToManyField(
        CustomUser,
        through="UserFavoriteGames"
    )
    game_image_url = models.CharField(max_length = 1000, default="")
    game_rating = models.CharField(max_length=20, default="...")
    posts = models.ManyToManyField(
        Post,
        through="GamePost"
    )
    genre = models.ManyToManyField(
        Genre,
        through="GameGenre"
    )

class UserFavoriteGames(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.PROTECT)
    game = models.ForeignKey(Game, on_delete=models.PROTECT)

class GameGenre(models.Model):
    game = models.ForeignKey(Game, on_delete=models.PROTECT)
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT)

class GamePost(models.Model):
    game = models.ForeignKey(Game, on_delete=models.PROTECT)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

class ProfilePicture(models.Model):
    user_id = models.ForeignKey(CustomUser, on_delete=models.PROTECT)
    media_id = models.ForeignKey(Media, on_delete=models.PROTECT)



    