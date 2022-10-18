from django.contrib import admin

from .models import Artist, Lyric, Song

# Register your models here.



class SongItemInline(admin.TabularInline):
    model = Song
    raw_id_fields = ['artist'] 




    
class ArtistAdmin(admin.ModelAdmin):
    search_fields = ['id', 'first_name', 'last_name', 'age']
    list_display = ['first_name', 'last_name', 'age']
    inlines = [SongItemInline]

    
    
class SongAdmin(admin.ModelAdmin):
    search_fields = ['artist', 'name', 'released_date', 'likes']
    list_display = ['name', 'artist', 'released_date', 'likes']
    
        
class LyricAdmin(admin.ModelAdmin):
    search_fields = ['song_id', 'artist']
    list_display = ['song_id', 'artist']

        
admin.site.register (Artist, ArtistAdmin)
admin.site.register (Song, SongAdmin)
admin.site.register (Lyric, LyricAdmin)