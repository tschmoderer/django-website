from django.contrib import admin

from .models import DBMusic

class DBMusicAdmin(admin.ModelAdmin): 
    list_display = ('title', 'filename')

admin.site.register(DBMusic, DBMusicAdmin)