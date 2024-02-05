from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    # '' == loachost:8000/project/pk
    path('', include('projects.urls'))
]
