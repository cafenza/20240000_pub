from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns =[
    path('main/', views.main),
    path('login/',auth_views.LoginView.as_view(template_name='member/login.html'),name='login'),#로그인 페이지 관련
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),#로그아웃 페이지 관련
    path('signup/',views.signup, name='signup'),#회원가입 관련된것
    

]