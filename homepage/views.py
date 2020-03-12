#-*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import Homepage

def home(request):
	return render(request, 'homepage/home.html')

def edit(request):
	query = Homepage.objects.all()
	context = {
		"homepage": query,
	}
	return render(request, 'homepage/edit.html', context)

def signup(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			login(request, user)
			return redirect('home')
	else:
		form = UserCreationForm()
	return render(request, 'signup.html', {'form': form})