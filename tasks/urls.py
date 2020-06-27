from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home_page'),
    path('update/<str:pk>/', views.update_item, name='update_page'),
    path('delete/<str:pk>/', views.delete_item, name='delete_page'),
    
]