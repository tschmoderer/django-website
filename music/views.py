#-*- coding: utf-8 -*-
from django.shortcuts import render, redirect, get_object_or_404
from homepage.models import Profile

def default(request, username = None):
	if not username == None: 
		profile  = get_object_or_404(Profile,  user__username =  username)
	else:
		profile  = None

	return render(request, 'music/network/index.html', {'profile': profile})