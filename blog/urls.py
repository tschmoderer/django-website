from django.urls import path
from . import views 

app_name = 'blog'

urlpatterns = [
	# re_path(r'^$', views.home, name='blog'),
	# re_path(r'^article/(?P<id>\d+)$', views.read, name="read"),
	# path('', views.home, name='home'),
	path('', views.ListArticles.as_view(), name='home'),
	path('article/<int:pk>', views.ReadArticle.as_view(), name='read_article'), 
	path('article/<int:pk>/edit', views.edit, name='edit'), 
	path('add/', views.add, name='add'),
]