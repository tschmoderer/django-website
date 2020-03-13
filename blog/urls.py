from django.urls import path
from . import views 

urlpatterns = [
	# re_path(r'^$', views.home, name='blog'),
	# re_path(r'^article/(?P<id>\d+)$', views.read, name="read"),
	path('', views.home, name='blog'),
	# path(r'article/(?P<id>\d+)', views.read, name="read"),
]