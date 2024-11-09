from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name = 'dash_path'),
    path('dashboard/order', views.order, name='order_path'),
    path('dashboard/profile', views.profile, name='profile_path'),

]
