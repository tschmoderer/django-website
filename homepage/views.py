#-*- coding: utf-8 -*-
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Homepage, Profile
from .forms import HomepageForm, ProfileForm, UserForm
from django.contrib.auth.decorators import login_required, permission_required
from django.http import Http404

def home(request, username = None):
	can_edit_profile  = False
	can_edit_homepage = False

	if not username == None: 
		profile  = get_object_or_404(Profile,  user__username =  username)
		homepage = get_object_or_404(Homepage, user__username =  username)
	else:
		profile  = None
		homepage = None

	if request.user.is_authenticated:
		if request.user.has_perm('homepage.can_edit_profile_{0}'.format(profile.user_id)):
			can_edit_profile = True
		
		if request.user.has_perm('homepage.can_edit_homepage_{0}'.format(profile.user_id)):
			can_edit_homepage = True

	context = {'profile': profile, 'homepage': homepage, 'can_edit_profile': can_edit_profile, 'can_edit_homepage': can_edit_homepage}

	return render(request, 'homepage/home.html', context)

@login_required
# TODO: handle image upload
def edit_homepage(request, username = None):
	homepage = get_object_or_404(Homepage, user__username =  username)
	profile  = get_object_or_404(Profile,  user__username =  username)

	if not request.user.has_perm('homepage.can_edit_homepage_{0}'.format(homepage.user_id)):
		raise Http404

	if request.method == 'POST': 
		if 'update_homepage_form' in request.POST:
			hform = HomepageForm(data=request.POST, instance=homepage)
			
			if hform.is_valid():
				hform.save()
				return redirect('homepage:home', username=profile.user.username)
		# handle cancel button
		else:
			return redirect('homepage:home', username=profile.user.username)

	else:
		hform = HomepageForm(instance = homepage)
	
	return render(request, 'homepage/edit_homepage.html', {'form_homepage': hform, 'profile': profile})

@login_required
def edit_profile(request, username = None):
	profile  = get_object_or_404(Profile,  user__username =  username)

	if not request.user.has_perm('homepage.can_edit_profile_{0}'.format(profile.user_id)):
		raise Http404

	if request.method == 'POST': 
		if 'update_profile_form' in request.POST:
			pform = ProfileForm(data=request.POST, files=request.FILES, instance=profile)
			uform = UserForm(data=request.POST, instance=profile.user)

			if uform.is_valid():
				uform.save()
			else: 
				render(request, 'homepage/edit_profile.html', {'form_profile': pform, 'form_user': uform, 'profile': profile})

			if pform.is_valid():
				profile = pform.save(commit=False)

				if 'clear_picture' in request.POST:
					profile.picture.delete()
					
				profile.save()
			else: 
				render(request, 'homepage/edit_profile.html', {'form_profile': pform, 'form_user': uform, 'profile': profile})

			return redirect('homepage:home', username=profile.user.username)

	else:
		uform = UserForm(instance     = profile.user)
		pform = ProfileForm(instance  = profile)
	
	return render(request, 'homepage/edit_profile.html', {'form_profile': pform, 'form_user': uform, 'profile': profile})