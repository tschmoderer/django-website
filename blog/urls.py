from django.urls import path, re_path
from . import views 

urlpatterns = [
	re_path(r'^$', views.home, name='blog'),
	re_path(r'^article/(?P<id>\d+)$', views.read, name="read"),
]

