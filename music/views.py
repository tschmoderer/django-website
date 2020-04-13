#-*- coding: utf-8 -*-
from django.shortcuts import render, redirect, get_object_or_404
from homepage.models import Profile
from .models import DBMusic, MusicPicture
from django.views.generic import ListView, DetailView

class ListDB(ListView):
	model = DBMusic
	context_object_name = 'databases'
	def get_context_data(self, **kwargs):
		# Call the base implementation first to get a context
		context = super().get_context_data(**kwargs)
		# Add in a QuerySet of all the books
		context['profile'] = get_object_or_404(Profile,  user__username = self.kwargs['username'])
		return context

class DisplayDB(DetailView): 
	model = DBMusic
	context_object_name = 'database'
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['profile'] = get_object_or_404(Profile,  user__username = self.kwargs['username'])
		return context

def default(request, username = None):
	if not username == None: 
		profile  = get_object_or_404(Profile,  user__username =  username)
		
	else:
		profile  = None

	return render(request, 'music/network/index.html', {'profile': profile})

def viewdb(request, username = None, dbname = None): 
	pass
