#-*- coding: utf-8 -*-
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Homepage, Profile

default_str = '/tschmoderer/'

def default(request): 
	# temporary
	return redirect(default_str)

def login_view(request):
	if request.method == 'POST':
		form = AuthenticationForm(data = request.POST)
		if form.is_valid():
			user = form.get_user()
			login(request, user)
			return redirect('/' + str(user.username) + '/')
	else:
		form = AuthenticationForm()
	return render(request, 'homepage/login.html', {'form': form})		

def logout_view(request): 
	if request.method == 'POST': 
		logout(request)
		return redirect(default_str)

def signup_view(request): 
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			Profile(user  = user).save()
			Homepage(user = user).save()
			login(request, user)
			return redirect('/' + str(user.username) + '/')
	else:
		form = UserCreationForm()
	return render(request, 'homepage/signup.html', {'form': form})

def home(request, username = None):
	if not username == None: 
	#    try:
    # 	   obj = MyModel.objects.get(pk=1)
    # except MyModel.DoesNotExist:
    #    raise Http404("No MyModel matches the given query.")

		profile  = get_object_or_404(Profile, user__username =  username)
		homepage = get_object_or_404(Homepage, user__username =  username)
	else:
		profile = None
		homepage = None
	# if tschmoderer --> return the right profile
	# for the moment default 
	return render(request, 'homepage/home.html', {'profile': profile, 'homepage': homepage, 'username':username})

def edit_homepage(request, username = None):
	homepage = get_object_or_404(Homepage, user__username =  username)
	return render(request, 'homepage/edit.html', {'homepage': homepage})