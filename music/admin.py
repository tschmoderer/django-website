from django.contrib import admin

from .models import DBMusic, MusicPicture

@admin.register(DBMusic)
class DBMusicAdmin(admin.ModelAdmin): 
    list_display = ('title', 'filename')

@admin.register(MusicPicture)
class MusicPictureAdmin(admin.ModelAdmin): 
    list_display = ('title', 'date_publi')
