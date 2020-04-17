#-*- coding: utf-8 -*-
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Homepage, Profile
from .forms import HomepageForm, ProfileForm, UserForm
from django.contrib.auth.decorators import login_required

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
	return render(request, 'homepage/login.html', {'login_form': form})		

def logout_view(request): 
	if request.method == 'POST':
		username = request.user.username 
		logout(request)
		return redirect('/' + str(username) + '/')

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
		profile  = get_object_or_404(Profile,  user__username =  username)
		homepage = get_object_or_404(Homepage, user__username =  username)
	else:
		profile  = None
		homepage = None

	return render(request, 'homepage/home.html', {'profile': profile, 'homepage': homepage})

@login_required
def edit_homepage(request, username = None):
	homepage = get_object_or_404(Homepage, user__username =  username)
	profile  = get_object_or_404(Profile,  user__username =  username)

	if request.method == 'POST': 
		if 'update_homepage_form' in request.POST:
			hform = HomepageForm(data=request.POST, instance=homepage)
			pform = ProfileForm(instance=profile)
			uform = UserForm(instance=profile.user)
			
			if hform.is_valid():
				hform.save()

		# handle cancel button
		else:
			hform = HomepageForm(instance = homepage)

	else:
		hform = HomepageForm(instance = homepage)
	
	return render(request, 'homepage/edit_homepage.html', {'form_homepage': hform, 'profile': profile})

@login_required
def edit_profile(request, username = None):
	profile  = get_object_or_404(Profile,  user__username =  username)

	if request.method == 'POST': 
		if 'update_user_form' in request.POST: 
			uform = UserForm(data=request.POST, instance=profile.user)
			pform = ProfileForm(instance  = profile)

			if uform.is_valid():
				uform.save()


		elif 'update_profile_form' in request.POST: 
			pform = ProfileForm(data=request.POST, files=request.FILES, instance=profile)
			uform = UserForm(instance = profile.user)

			if pform.is_valid():
				profile = pform.save(commit=False)

				if 'clear_picture' in request.POST:
					profile.picture = profile.__class__._meta.get_field('picture').default
					
				profile.save()
				
		# handle cancel button
		else:
			uform = UserForm(instance     = profile.user)
			pform = ProfileForm(instance  = profile)


	else:
		uform = UserForm(instance     = profile.user)
		pform = ProfileForm(instance  = profile)
	
	return render(request, 'homepage/edit_profile.html', {'form_profile': pform, 'form_user': uform, 'profile': profile})