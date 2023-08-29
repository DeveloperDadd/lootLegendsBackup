# Generated by Django 4.2.3 on 2023-08-21 13:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lootlegends', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_title', models.CharField(max_length=255)),
                ('rawg_id', models.IntegerField()),
                ('game_cover_art', models.CharField()),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre_type', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField()),
                ('asset_url', models.CharField()),
                ('date_uploaded', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_text', models.CharField(max_length=140)),
                ('date_posted', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=16)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=16)),
                ('date_registered', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='UserFavoriteGames',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lootlegends.game')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lootlegends.user')),
            ],
        ),
        migrations.CreateModel(
            name='ProfilePicture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('media_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lootlegends.media')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lootlegends.user')),
            ],
        ),
        migrations.CreateModel(
            name='PostMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('media', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lootlegends.media')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lootlegends.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lootlegends.user')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lootlegends.user'),
        ),
        migrations.AddField(
            model_name='media',
            name='user_id',
            field=models.ManyToManyField(through='lootlegends.PostMedia', to='lootlegends.user'),
        ),
        migrations.CreateModel(
            name='GamePost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lootlegends.game')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lootlegends.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lootlegends.user')),
            ],
        ),
        migrations.CreateModel(
            name='GameGenre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lootlegends.game')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lootlegends.genre')),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='genre',
            field=models.ManyToManyField(through='lootlegends.GameGenre', to='lootlegends.genre'),
        ),
        migrations.AddField(
            model_name='game',
            name='posts',
            field=models.ManyToManyField(through='lootlegends.GamePost', to='lootlegends.post'),
        ),
        migrations.AddField(
            model_name='game',
            name='user',
            field=models.ManyToManyField(through='lootlegends.UserFavoriteGames', to='lootlegends.user'),
        ),
    ]
