from django.contrib import admin
from django.urls import path, include 
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    # '' == loachost:8000/project/pk
    path('projects/', include('projects.urls')),
    # localhost:8000/users
    path('', include('users.urls')),
    path('api/', include('api.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)