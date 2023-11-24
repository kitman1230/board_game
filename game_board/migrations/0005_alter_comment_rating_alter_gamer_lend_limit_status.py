# Generated by Django 4.2.7 on 2023-11-11 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game_board', '0004_alter_boardgame_age_limit_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='rating',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Bad'), (2, 'Soso'), (3, 'Normal'), (4, 'Good'), (5, 'Excellent')]),
        ),
        migrations.AlterField(
            model_name='gamer',
            name='lend_limit_status',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Zero'), (1, 'One'), (2, 'Two'), (3, 'Three')]),
        ),
    ]
