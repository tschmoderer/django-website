from django.shortcuts import get_object_or_404, redirect, render
from homepage.models import Profile
from .models import Project
from .forms import ProjectForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required

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

class DetailProject(DetailView):
	model = Project
	context_object_name = 'project'
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['profile'] = get_object_or_404(Profile,  user__username = self.kwargs['username'])
		return context

class UpdateProject(UpdateView):
	model = Project
	form_class = ProjectForm
	template_name_suffix = '_update'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['profile'] = get_object_or_404(Profile,  user__username = self.kwargs['username'])
		context['id']  = self.kwargs['pk']
		context['prj'] = get_object_or_404(Project, id=context['id'])# Project.objects.filter(id = context['id'])
		return context
	
	def post(self, request, *args, **kwargs):
		prj = get_object_or_404(Project, id = self.kwargs['pk'])

		form    = self.form_class(request.POST, files=request.FILES, instance=prj)
		profile = get_object_or_404(Profile,  user__username = self.kwargs['username'])

		# Check form validation
		if form.is_valid(): # TODO: clear picture (comme dans homepage update profil)
			# prj = form.save(commit=False)
			# prj.author_id = profile.user.id
			prj.save()
			return redirect('projects:home', username = profile.user.username)

		return render(request, self.template_name, {'form': form, 'profile': profile})
	
	"""
	def get(self, request, *args, **kwargs): 
		form     = self.form_class(data=Project.objects.filter(id=self.kwargs['pk']))
		profile  = get_object_or_404(Profile,  user__username =  self.kwargs['username'])
		return render(request, self.template_name, {'form': form, 'profile': profile})
	"""

@login_required
def delete_project(request, username = None, pk = None): 
    profile  = get_object_or_404(Profile, user__username =  username)
    Project.objects.filter(id=pk).delete()
    return redirect('projects:home', username=profile.user.username)

@login_required
def create_project(request, username = None): 
	profile  = get_object_or_404(Profile,  user__username =  username)

	if request.method == 'POST':
		pform = ProjectForm(data=request.POST, files=request.FILES)

		if pform.is_valid():
			project = pform.save(commit=False)
			project.author_id = profile.user_id
			project.save()
			return redirect('projects:home', username=profile.user.username)

	else:
		pform = ProjectForm()
	return render(request, 'projects/create_project.html', {'form_project': pform, 'profile': profile})