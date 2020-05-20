#-*- coding: utf-8 -*-
from .models import Article
from .forms import ArticleForm
from django.shortcuts import get_object_or_404, redirect, render
from homepage.models import Profile
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required

class ListArticles(ListView):
	model = Article
	context_object_name = 'last_articles'
	ordering = ['-date_publi']
	paginate_by = 3
	def get_context_data(self, **kwargs):
		# Call the base implementation first to get a context
		context = super().get_context_data(**kwargs)
		# Add in a QuerySet of all the books
		context['profile'] = get_object_or_404(Profile,  user__username = self.kwargs['username'])
		return context

class ReadArticle(DetailView):
	model = Article
	context_object_name = 'article'
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['profile'] = get_object_or_404(Profile,  user__username = self.kwargs['username'])
		return context

class UpdateArticle(UpdateView):
    pass

@login_required
def delete_article(request, username = None, pk = None): 
    profile  = get_object_or_404(Profile, user__username =  username)
    Article.objects.filter(id=pk).delete()
    return redirect('blog:home', username=profile.user.username)

@login_required
def create_article(request, username = None): 
	profile  = get_object_or_404(Profile,  user__username =  username)

	if request.method == 'POST':
		aform = ArticleForm(data=request.POST)

		if aform.is_valid():
			article = aform.save(commit=False)
			article.author_id = profile.user_id
			article.save()
			return redirect('blog:home', username=profile.user.username)

	else:
		aform = ArticleForm()
	return render(request, 'blog/create_article.html', {'form_article': aform, 'profile': profile})