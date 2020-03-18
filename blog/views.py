#-*- coding: utf-8 -*-
from .models import Article
from django.shortcuts import render, get_object_or_404
from homepage.models import Profile

def home(request, username = None):
	profile  = get_object_or_404(Profile,  user__username =  username)
	articles = [] # Article.objects.all()
	return render(request, 'blog/home.html', {'last_articles':articles, 'profile': profile})

def read(request, id):
	pass