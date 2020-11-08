from django.urls import include, path

from . import views

app_name = 'projects'

urlpatterns = [
	# path('', views.home, name='home'),
	path('', views.ListProjects.as_view(), name='home'),
	path('create/', views.create_project, name='create_project'),
	path('detail/<int:pk>', views.DetailProject.as_view(), name='detail_project'), 
	path('update/<int:pk>', views.UpdateProject.as_view(), name='update_project'),
	path('delete/<int:pk>', views.delete_project, name='delete_project'),
]
