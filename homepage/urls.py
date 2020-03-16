from django.urls import include, path
from django.contrib.auth import views as auth_views
from . import views 

app_name = 'homepage'

urlpatterns = [
	# re_path(r'^$', views.home, name='home'),
	# re_path(r'^blog/', include('blog.urls')),
	# re_path(r'edit/', views.edit, name='edit'),
	# re_path(r'signup/', views.signup, name='signup'),
	# re_path(r'login/', auth_views.LoginView.as_view(template_name='homepage/login.html'), name='login'),
	# re_path(r'^logout/', auth_views.LogoutView.as_view(template_name='homepage/home.html'), name='logout'),

	# path(r'(?P<username>[^/]+)/', views.home, name='home'),
	# path('', views.home, name='home'),
	path('', views.default, name='default'),
	path('login/', views.login_view,    name='login'),
	path('logout/', views.logout_view,  name='logout'),
	path('signup/', views.signup_view,  name='signup'),
	path('<str:username>/', views.home, name='home'),
	path('<str:username>/edit/', views.edit_homepage, name='edit'),
	path('<str:username>/blog/', include('blog.urls')),
]