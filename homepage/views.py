#-*- coding: utf-8 -*-
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import Homepage, Profile

def default(request): 
	# temporary
	return redirect('/tschmoderer/')

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