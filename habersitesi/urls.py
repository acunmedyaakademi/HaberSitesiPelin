from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('contact/', views.contact, name="contact"),
    path('about/', views.about, name="about"),
    path('news/', views.news, name="news"),
    path('add_news/', views.add_news, name="add_news"),
    
]