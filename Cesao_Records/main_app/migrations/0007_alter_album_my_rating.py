# Generated by Django 4.1.7 on 2023-03-02 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_album_my_rating_album_my_review_alter_song_review_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='my_rating',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
