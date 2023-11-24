# Generated by Django 4.2.7 on 2023-11-11 12:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game_board', '0008_alter_boardgame_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='gamer',
            name='bio',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='gamer',
            name='firstname',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='gamer',
            name='lastname',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='gamer',
            name='username',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='boardgame',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game_board.gamer'),
        ),
    ]
