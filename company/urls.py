from django.urls import path
from . import  views

urlpatterns = [

    path('',views.home, name = 'home'),

    path('compins/', views.compins, name='compins'),
    path('editcompany/<int:Branch_Id>/', views.editcompany, name='editcompany'),
    path('deletecompany/<int:Branch_Id>/', views.deletecompany, name='deletecompany'),
    path('get_districts/<int:state_id>/', views.get_districts, name='get_districts'),

    path('stateins/', views.stateins, name='stateins'),
    path('stateedit/<int:stateid>/', views.stateedit, name='stateedit'),
    path('statedelete/<int:stateid>/', views.statedelete, name='statedelete'),

    path('district/', views.district, name='district'),
    path('editdist/<int:distid>/',views.editdist,name='editdist'),
    path('deletedist/<int:distid>/',views.deletedist,name='deletedist'),

    path('instype/', views.instype, name =  'instype'),
    path('editinstype/<int:InsType_Id>/',views.editinstype,name='editinstype'),
    path('deleteinstype/<int:InsType_Id>/',views.deleteinstype, name='deleteinstype'),

    path('claimins/', views.claimins,name='claimins'),
    path('editclaim/<int:CStatusCode>/',views.editclaim,name='editclaim'),
    path('deleteclaim/<int:CStatusCode>/', views.deleteclaim, name='deleteclaim'),

    path('policies/', views.policies, name='policies'),
    path('editdpolicy/<int:Policy_Id>/', views.editpolicy, name='editpolicy'),
    path('deletepolicy/<int:Policy_Id>/', views.deletepolicy, name='deletepolicy'),

    path('policyfeature/', views.policyfeature, name='policyfeature'),
    path('editdpf/<int:Feature_Id>/', views.editpf, name='editpf'),
    path('deletepf/<int:Feature_Id>/', views.deletepf, name='deletepf'),

    path('policybenefits/', views.policybenefits, name='policybenefits'),
    path('editdpb/<int:Benefit_id>/', views.editpb, name='editpb'),
    path('deletepb/<int:Benefit_id>/', views.deletepb, name='deletepb'),

    path('policydocuments/', views.policydocuments, name='policydocuments'),
    path('editdpd/<int:Docu_Id>/', views.editpd, name='editpd'),
    path('deletepd/<int:Docu_Id>/', views.deletepd, name='deletepd'),

    path('premode/', views.premode, name='premode'),
    path('editpre/<int:pre_mode_id>/', views.editpre, name='editpre'),
    path('deletepre/<int:pre_mode_id>/', views.deletepre, name='deletepre'),

    path('pc/', views.pc, name='pc'),
    path('editpc/<int:PolComId>/', views.editpc, name='editpc'),
    path('deletepc/<int:PolComId>/', views.deletepc, name='deletepc'),

    path('pp/', views.pp, name='pp'),
    path('editpp/<int:pol_pre_id>/', views.editpp, name='editpp'),
    path('deletepp/<int:pol_pre_id>/', views.deletepp, name='deletepp'),

    path('sa/', views.sa, name='sa'),
    path('editsa/<int:sum_assureid>/', views.editsa, name='editsa'),
    path('deletesa/<int:sum_assureid>/', views.deletesa, name='deletesa'),

    path('news/', views.news, name='news'),
    path('editnews/<int:newsid>/', views.editnews, name='editnews'),
    path('deletenews/<int:newsid>/', views.deletenews, name='deletenews'),

    path('claims/', views.claims, name='claims'),
    path('editclaims/<int:claim_id>/', views.editclaims, name='editclaims'),
    path('deleteclaims/<int:claim_id>/', views.deleteclaims, name='deleteclaims'),

    #TEMPLATE URLS
    path('thome/', views.thome, name='thome'),
    path('cabout/', views.cabout, name= 'cabout'),
    path('cservices/', views.cservices, name='cservices'),
    path('user_logout/', views.user_logout, name='user_logout'),

    path('admin_policy_view/<int:policy_id>/', views.admin_policy_view, name='admin_policy_view'),
    path('view_document/<int:customer_id>/<int:policy_id>/', views.view_document, name='view_document'),
    path('verify_document/<int:poldoc_id>/', views.verify_document,name='verify_document'),
    path('view_claim_details/',views.view_claim_details,name='view_claim_details'),
    path('verify_claim/<int:claim_id>/',views.verify_claim,name='verify_claim'),
]

