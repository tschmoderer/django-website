from django.urls import include, path
from django.contrib.auth import views as auth_views
from . import views 

app_name = 'homepage'

urlpatterns = [
	path('', views.default, name='default'),
	path('login/', views.login_view,    name='login'),
	path('logout/', views.logout_view,  name='logout'),
	path('signup/', views.signup_view,  name='signup'),
	path('<str:username>/', views.home, name='home'),
	path('<str:username>/edit_homepage/', views.edit_homepage, name='edit_homepage'),
	path('<str:username>/edit_profile/', views.edit_profile, name='edit_profile'),

	path('<str:username>/blog/', include('blog.urls', namespace='blog')),
	path('<str:username>/music/', include('music.urls', namespace='music')),
]