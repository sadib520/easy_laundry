from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name = 'dash_path'),
    path('dashboard/order', views.order, name='order_path'),
    path('dashboard/profile', views.profile, name='profile_path'),
    path('dashboard/select_quantity/', views.quantity, name='quantity_path'),
    path('dashboard/payment', views.payment, name='payment_path'),
    path('dashboard/buy_plan', views.buyplan, name='plan_path'),
    # path('dashboard/bill', views.bill, name='bill_path'),
    path('dashboard/profile/update_info', views.update_profile_info, name='update_path'),

]
