from django.urls import path
from .import views

urlpatterns = [
    path('loginUser/', views.loginUser, name = 'loginUser'),
    path('logoutUser/', views.logoutUser, name = 'logoutUser'),
    path('registerUser/', views.registerUser , name = 'registerUser'),
    path('', views.main, name='main'),
    path('about/', views.about, name='aboutUs'),
    path('bayel/', views.bayel, name='bayelCon'),
]