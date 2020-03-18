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
	path('<str:username>/edit/', views.edit_homepage, name='edit'),
	path('<str:username>/blog/', include('blog.urls')),
]