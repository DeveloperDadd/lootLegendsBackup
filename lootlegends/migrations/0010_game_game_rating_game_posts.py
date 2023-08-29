# Generated by Django 4.2.3 on 2023-08-28 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lootlegends', '0009_remove_game_posts'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='game_rating',
            field=models.CharField(default='...', max_length=20),
        ),
        migrations.AddField(
            model_name='game',
            name='posts',
            field=models.ManyToManyField(through='lootlegends.GamePost', to='lootlegends.post'),
        ),
    ]
