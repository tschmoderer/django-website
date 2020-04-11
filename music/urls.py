from django.urls import include, path
from django.contrib.auth import views as auth_views
from . import views 

app_name = 'music'

urlpatterns = [
	path('', views.ListDB.as_view(), name='home'),
	path('db/<int:pk>', views.DisplayDB.as_view(), name='show_db'), 
]