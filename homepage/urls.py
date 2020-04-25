from django.urls import include, path

from . import views

app_name = 'homepage'

urlpatterns = [
	path('', views.home, name='home'),
	path('edit_homepage/', views.edit_homepage, name='edit_homepage'),
	path('edit_profile/',  views.edit_profile,   name='edit_profile'),
]
