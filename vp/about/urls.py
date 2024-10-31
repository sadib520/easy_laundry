from django.urls import path 
from . import views

urlpatterns = [
    path('about/', views.about, name = 'about_path'),
    path('laundry/', views.laundry, name='laundry_path'),
    path('ironing/', views.iron, name='iron_path'),
    path('dry_cleaning/', views.dry, name='dry_path'),
]
