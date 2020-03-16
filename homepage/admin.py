from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
# My models 
from .models import Homepage, Profile

class HomepageModelAdmin(admin.ModelAdmin): 
    list_display = ["title", "date_modif"]

# admin.site.register(Homepage, HomepageModelAdmin)
admin.site.register(Homepage, MarkdownxModelAdmin)
admin.site.register(Profile)