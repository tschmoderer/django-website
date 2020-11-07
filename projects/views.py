from django.shortcuts import get_object_or_404, redirect, render
from homepage.models import Profile
from .models import Project
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

# Create your views here.
def home(request, username = None):
	if not username == None: 
		profile  = get_object_or_404(Profile,  user__username =  username)
	else:
		profile  = None

	context = {'profile': profile}

	return render(request, 'projects/home.html', context)

def pack(_list):
	_list = list(_list)
	new_list = list(zip(_list[::2], _list[1::2]))
	if (len(_list) % 2) == 1:
		new_list.append((_list[-1], None))
	return new_list

class ListProjects(ListView):
	model = Project
	context_object_name = 'last_projects'
	ordering = ['-date_publi']
	def get_context_data(self, **kwargs):
		# Call the base implementation first to get a context
		context = super().get_context_data(**kwargs)
		context['last_projects_by_2'] = pack(context['last_projects'])
		# Add in a QuerySet of all the books
		context['profile'] = get_object_or_404(Profile,  user__username = self.kwargs['username'])
		return context

def wheels(request, username = None): 
	profile  = get_object_or_404(Profile,  user__username =  username)
	return render(request, 'projects/wheels.html', {'profile': profile})