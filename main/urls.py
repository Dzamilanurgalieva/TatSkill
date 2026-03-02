from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('education/', views.education, name='education'),
    path('travel/', views.travel, name='travel'),
    path('ratings/', views.ratings, name='ratings'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
]