from django.urls import include, path

from . import views

app_name = 'projects'

urlpatterns = [
	# path('', views.home, name='home'),
	path('', views.ListProjects.as_view(), name='home'),
	path('wheels/', views.wheels, name='wheels')
]
