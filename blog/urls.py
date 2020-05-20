from django.urls import include, path

from . import views

app_name = 'blog'

urlpatterns = [
	path('', views.ListArticles.as_view(), name='home'),
	path('create/', views.create_article, name='create_article'),
	path('read/<int:pk>', views.ReadArticle.as_view(), name='read_article'), 
	path('update/<int:pk>', views.UpdateArticle.as_view(), name='update_article'), 
	path('delete/<int:pk>', views.delete_article, name='delete_article'),
]