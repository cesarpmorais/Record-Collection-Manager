# Generated by Django 4.1.7 on 2023-03-02 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_song_composer_alter_song_length'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='my_rating',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='album',
            name='my_review',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='review',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
        migrations.AddConstraint(
            model_name='album',
            constraint=models.CheckConstraint(check=models.Q(('my_rating__gte', 0.0), ('my_rating__lte', 10.0)), name='my_rating_range'),
        ),
    ]