from django.urls import path
from . import views 

urlpatterns = [
	path(r'', views.home),
	path(r'about', views.home), 
	path(r'about.html', views.home),
]

