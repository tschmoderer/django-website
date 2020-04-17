#-*- coding: utf-8 -*-
from .models import Article
from .forms import ArticleForm
from django.shortcuts import render, get_object_or_404, redirect
from homepage.models import Profile
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView

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

@login_required
def edit_article(request, username = None, pk = None): 
	profile  = get_object_or_404(Profile, user__username =  username)
	article  = get_object_or_404(Article, id = pk)

	if request.method == 'POST':
		if 'edit_article_form' in request.POST:
			aform = ArticleForm(request.POST, instance=article)
			if aform.is_valid():
				aform.save()
				return redirect('homepage:blog:read_article', username=profile.user.username, pk=article.id)
		else: 
			return redirect('homepage:blog:read_article', username=profile.user.username, pk=article.id)
	else:
		aform = ArticleForm(instance=article)
	
	return render(request, 'blog/edit.html', {'form_article': aform, 'profile': profile, 'article': article})

@login_required
def add_article(request, username = None):
	profile  = get_object_or_404(Profile, user__username =  username)

	if request.method == 'POST': 
		if 'add_article_form' in request.POST:
			aform = ArticleForm(request.POST)
			if aform.is_valid():
				article = aform.save(commit=False)
				article.author_id = profile.user.id
				article.save()
				return redirect('homepage:blog:home', username=profile.user.username)

		else:
			return redirect('homepage:blog:home', username=profile.user.username)
			
	else:
		aform = ArticleForm()
	
	return render(request, 'blog/add.html', {'form_article': aform, 'profile': profile})

@login_required
def delete_article(request, username = None, pk = None): 
	profile  = get_object_or_404(Profile, user__username =  username)
	Article.objects.filter(id=pk).delete()
	return redirect('homepage:blog:home', username=profile.user.username)