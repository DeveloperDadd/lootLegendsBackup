# Generated by Django 4.2.3 on 2023-08-25 04:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lootlegends', '0005_rename_game_image_game_game_image_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='game_description',
        ),
    ]
