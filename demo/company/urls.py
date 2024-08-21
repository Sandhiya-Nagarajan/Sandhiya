from django.urls import path
from. import views

urlpatterns=[
    path('',views.registerpage),
    path('userlogin/', views.userlogin,),
    path('adminlogin/',views.adminlogin),
    path('adminhome/',views.adminhome),
    path('pending/',views.pending),
    path('approve/<int:id>',views.approve),
    path('approved/',views.approved),
    path('operations/',views.operations),
]