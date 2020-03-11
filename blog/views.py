#-*- coding: utf-8 -*-
from django.shortcuts import render
from blog.models import Article

def home(request):
	articles = Article.objects.all()
	return render(request, 'blog/home.html', {'last_articles':articles})

def read(request, id):
	pass