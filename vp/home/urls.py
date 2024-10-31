from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name ='home_path'),
    path('developers/', views.cards, name = 'dev_path'),
    path('join_us/', views.join, name = 'join_path'),
    path('contact/', views.contact, name='contact_path'),
    path('postal_code/check/', views.check_postal_code, name='postal_path')
]
