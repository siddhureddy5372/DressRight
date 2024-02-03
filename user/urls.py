from django.urls import path
from . import views

urlpatterns = [
    path("",views.login,name="index"),
    path("register",views.register, name="register"),
    path("logout", views.logout, name= "logout"),
    path('profile', views.profile, name='profile'),
]