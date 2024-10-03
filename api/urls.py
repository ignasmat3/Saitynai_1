from django.urls import path
from .import views

urlpatterns = [
    path('user/', views.get_user),
    path('user/create', views.create_user),# Add your URL patterns here
]