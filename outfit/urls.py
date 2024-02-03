from django.urls import path
from . import views
from closet.views import cloths_detail

urlpatterns = [
    path("home", views.suggest_outfit, name="home" ),
    path("count", views.count,name="count"),
    path("worn",views.increment_worn_count, name="worn"),
]