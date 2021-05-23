from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
     path('searchFromQuran', views.searchQuery),
    #path('home', views.home)
    
]