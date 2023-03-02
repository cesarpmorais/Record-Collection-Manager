from django.contrib import admin
from main_app.models import Collection, Artist, Song, Album, Record


class SongInline(admin.TabularInline):
    model = Song
    fields = ['name', 'composer', 'length']


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('name', 'artist_name','release_date',)
    inlines = (SongInline, )
    
    def artist_name(self, obj):
        return obj.artist.name
    
    
@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('name', 'country_of_origin')
    
    
@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ('name',)
    
    
@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ('album_name', 'pressing_year', 'cover_rating', 'disc_rating')
    
    def album_name(self, obj):
        return obj.album.name


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ('name', 'album_name', 'length')
    
    def album_name(self, obj):
        return obj.album.name