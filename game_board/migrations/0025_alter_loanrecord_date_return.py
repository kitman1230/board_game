# Generated by Django 4.2.7 on 2023-11-13 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game_board', '0024_remove_boardgame_artist_remove_boardgame_designer_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loanrecord',
            name='date_return',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
