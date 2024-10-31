from django.urls import path
from . import views


urlpatterns = [
    path('login_page/', views.log_in_page, name='login_path'),
    path('registration/', views.reg, name='reg_path'),
    path('info_saved/', views.add_user, name='adduser_path'),
    path('greet/', views.greet, name='greet_path'),
    path('logout/', views.logout, name='logout_path')

]
