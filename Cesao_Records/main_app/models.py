from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db.models import CheckConstraint, Q

# Create your models here.
class Collection(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField(max_length=255)
    
    def __str__(self):
        return self.name
  

class Artist(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    country_of_origin = models.CharField(max_length=255)  
    
    def __str__(self):
        return self.name
    
    
class Album(models.Model):
    id = models.BigAutoField(primary_key=True)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    release_date = models.DateField()
    description = models.TextField()
    length = models.CharField(max_length=5)
    
    my_review = models.TextField(max_length=1000, null=True, blank=True)
    my_rating = models.FloatField(null=True, blank=True)
    
    class Meta:
        constraints = (
            CheckConstraint(
                check=Q(my_rating__gte=0.0) & Q(my_rating__lte=10.0),
                name='my_rating_range'),
            )
    
    def __str__(self):
        return self.name

    
class Song(models.Model):
    id = models.BigAutoField(primary_key=True)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    composer = models.CharField(max_length=255, null=True)
    length = models.CharField(max_length=5)
    review = models.TextField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name
    
    
class Record(models.Model):
    id = models.BigAutoField(primary_key=True)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE,)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, null=True)
    country_of_origin = models.CharField(max_length=20)
    pressing_year = models.CharField(max_length=4)
    
    class Channels(models.TextChoices):
        STEREO = 'Stereo', _('Stereo')
        MONO = 'Mono', _('Mono')
        
    channels = models.CharField(max_length=20, choices=Channels.choices, null=True)
    
    class Ratings(models.TextChoices):
        MINT = 'Mint', _('M')
        NEAR_MINT = 'Near Mint', _('NM')
        VERY_GOOD_PLUS = 'Very Good +', _('VG+')
        VERY_GOOD = 'Very Good', _('VG')
        GOOD = 'Good', _('G')
        POOR = 'Poor', _('P')

    cover_rating = models.CharField(max_length=20, choices=Ratings.choices)
    disc_rating = models.CharField(max_length=20, choices=Ratings.choices)
    
    obs = models.TextField(max_length=255)
    
    def __str__(self):
        return self.album.name