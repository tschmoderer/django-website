from django.urls import path
from . import views 

app_name = 'blog'

urlpatterns = [
	# re_path(r'^$', views.home, name='blog'),
	# re_path(r'^article/(?P<id>\d+)$', views.read, name="read"),
	path('', views.home, name='home'),
	# path(r'article/(?P<id>\d+)', views.read, name="read"),
]