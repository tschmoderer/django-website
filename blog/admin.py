from django.contrib import admin
from .models import Article

@admin.register(Article)
class ArticleModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_modif')