from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.views.generic.base import RedirectView

urlpatterns = [
    # Administration of the website
    path('admin/', admin.site.urls),

    # urls routage
    # path('', include('site_base.urls', namespace='base')),
    # path('<str:username>/', include('homepage.urls', namespace='homepage')),
    # path('<str:username>/blog/', include('blog.urls', namespace='blog')),
    path('', RedirectView.as_view(url='tschmoderer', permanent=False), name='index'),
    path('<str:username>/', include('homepage.urls', namespace='homepage')),
    # external tool urls
] 

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)