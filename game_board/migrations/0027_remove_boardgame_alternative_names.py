# Generated by Django 4.2.7 on 2023-11-14 09:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game_board', '0026_remove_boardgame_category_boardgame_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='boardgame',
            name='alternative_names',
        ),
    ]
