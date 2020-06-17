from django.urls import path, include
from . import views as basic_views

urlpatterns = [
    path("", basic_views.home, name="home"),
]
