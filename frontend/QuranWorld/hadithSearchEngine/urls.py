from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('searchFromHadith', views.searchHadith),
    #path('home', views.home)
    
]