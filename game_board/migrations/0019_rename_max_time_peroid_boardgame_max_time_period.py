# Generated by Django 4.2.7 on 2023-11-11 17:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game_board', '0018_alter_profile_birthday'),
    ]

    operations = [
        migrations.RenameField(
            model_name='boardgame',
            old_name='max_time_peroid',
            new_name='max_time_period',
        ),
    ]
