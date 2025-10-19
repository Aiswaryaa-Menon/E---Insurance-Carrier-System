from django.urls import path
from . import  views

urlpatterns = [
    path('', views.placeholder_view,name='placeholder_view'),  # Just to keep Django happy for now
    path('register_agent/', views.register_agent,name='register_agent'),
    path('register_customer/',views.register_customer,name='register_customer'),
    path('login_view/', views.login_view, name='login_view'),

]