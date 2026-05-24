from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('login/', views.LoginInterfaceView.as_view(), name='login'),
    path('logout/', views.LogoutInterfaceView.as_view(), name='logout'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('farewell/', views.FarewellView.as_view(), name='farewell'),
]