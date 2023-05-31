from django.contrib import admin
from django.urls import path
from vier_node import views

urlpatterns = [
    path('', views.index, name="home"),
    path('pricing', views.pricing, name="pricing"),
    path('about', views.about, name="about"),
    path('contact', views.contact, name="contact"),
    path('gallery', views.gallery, name="gallery"),
     path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('dashboard', views.dashboard, name="dashboard"),
    path('thanks', views.thanks, name="thanks"),
    path('news_letter', views.news_letter, name="news_letter")
]
