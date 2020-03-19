from django.contrib import admin

# My models 
from markdownx.admin import MarkdownxModelAdmin
from .models import Article

@admin.register(Article)
class ArticleModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_modif')