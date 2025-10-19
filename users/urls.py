from django.urls import path
from . import  views


urlpatterns = [

    path('',views.home2, name = 'home2'),

    path('cust/',views.cust, name='cust'),
    path('editcust/<int:customer_id>/', views.editcust, name='editcust'),
    path('deletecust/<int:customer_id>/', views.deletecust, name='deletecust'),

    path('cpol/',views.cpol, name='cpol'),
    path('editcpol/<int:cpol_id>/', views.editcpol, name='editcpol'),
    path('deletecpol/<int:cpol_id>/', views.deletecpol, name='deletecpol'),

    path('cdoc/',views.cdoc, name='cdoc'),
    path('editcdoc/<int:poldoc_id>/', views.editcdoc, name='editcdoc'),
    path('deletecdoc/<int:poldoc_id>/', views.deletecdoc, name='deletecdoc'),

    path('pres/', views.pres, name='pres'),
    path('editpres/<int:schedule_id>/', views.editpres, name='editpres'),
    path('deletepres/<int:schedule_id>/', views.deletepres, name='deletepres'),

    path('pm/', views.pm, name='pm'),
    path('editpm/<int:payment_id>/', views.editpm, name='editpm'),
    path('deletepm/<int:payment_id>/', views.deletepm, name='deletepm'),

    path('comp/', views.comp, name='comp'),
    path('editcomp/<int:comp_id>/', views.editcomp, name='editcomp'),
    path('deletecomp/<int:comp_id>/', views.deletecomp, name='deletecomp'),

    path('user_home/', views.user_home, name='user_home'),
    path('policy_detail/<int:policy_id>/', views.policy_detail, name='policy_detail'),
    path('buy_policy/<int:policy_id>/', views.buy_policy, name='buy_policy'),
    path('upload_documents/<int:policy_id>/', views.upload_documents, name='upload_documents'),
    path('success/', views.success, name='success'),
    path('choose_premium_mode/<int:policy_id>/', views.choose_premium_mode, name='choose_premium_mode'),
    path('premium_pay/',views.premium_pay,name='premium_pay'),
    path('view_schedule/<int:customer_id>/',views.view_schedule,name='view_schedule'),
    path('make_payment/',views.make_payment,name='make_payment'),
    path('pay_success/<int:schedule_id>/', views.pay_success,name='pay_success'),
    path('complaint',views.complaint,name='complaint'),
    path('seenews',views.seenews,name='seenews'),
    path('news_detail/<int:newsid>/',views.news_detail,name='news_detail'),
    path('file_claim/', views.file_claim,name='file_claim'),
    path('user_dashboard/',views.user_dashboard,name='user_dashboard'),
    path('edit_profile/',views.edit_profile,name='edit_profile'),
    path('user_policies/',views.user_policies,name='user_policies'),
    path('my_claims/',views.my_claims,name='my_claims'),
]