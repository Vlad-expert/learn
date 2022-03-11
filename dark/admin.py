from django.contrib import admin
from .models import News, Band, MusicAlbum, Tracks
# Register your models here.


class NewsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


class BandAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class MusicAlbumAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class TracksAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}    

admin.site.register(News, NewsAdmin)  
admin.site.register(Band, BandAdmin) 
admin.site.register(MusicAlbum, MusicAlbumAdmin)    
admin.site.register(Tracks, TracksAdmin)    

