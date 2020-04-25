from django.contrib import admin
# My models 
from .models import Homepage, Profile

admin.site.register(Homepage)
admin.site.register(Profile)