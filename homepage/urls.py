from django.urls import re_path
from django.contrib.auth import views as auth_views
from . import views 

urlpatterns = [
	re_path(r'^$', views.home, name='home'),
	# re_path(r'edit/', views.edit, name='edit'),
	# re_path(r'signup/', views.signup, name='signup'),
	re_path(r'login/', auth_views.LoginView.as_view(template_name='homepage/login.html'), name='login'),
	re_path(r'logout/', auth_views.LogoutView.as_view(template_name='homepage/logout.html'), name='logout'),
]