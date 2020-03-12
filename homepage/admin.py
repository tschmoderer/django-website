from django.contrib import admin

# My models 
from .models import Homepage, Profile

class HomepageModelAdmin(admin.ModelAdmin): 
    list_display = ["title", "date_modif"]

admin.site.register(Homepage, HomepageModelAdmin)
admin.site.register(Profile)