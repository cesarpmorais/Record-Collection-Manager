# Generated by Django 4.1.7 on 2023-03-02 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='name',
            field=models.TextField(max_length=255, null=True),
        ),
    ]
