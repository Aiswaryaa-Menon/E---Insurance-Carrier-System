from django.urls import path
from . import  views

urlpatterns = [

    path('',views.home1, name = 'home1'),
    path('ap/',views.ap,name='ap'),
    path('editap/<int:PolicyNo>/',views.editap, name='editap'),
    path('deleteap/<int:PolicyNo>/', views.deleteap,name='deleteap'),
    path('agent_dashboard/', views.agent_dashboard,name='agent_dashboard'),
    path('view_commission/', views.view_commission,name='view_commission'),
    path('view_my_policies/', views.view_my_policies,name='view_my_policies'),
    path('agent_dashboard/', views.agent_dashboard,name='agent_dashboard'),
    path('agent_buy_policy/<int:policy_id>/', views.agent_buy_policy,name='agent_buy_policy'),



]