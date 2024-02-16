from django.urls import path
from . import views

urlpatterns = [
     # localhost:8000/users
    path('', views.profiles, name="profiles"),
    path('profile/<str:pk>', views.userProfile, name="user-profile"),

]