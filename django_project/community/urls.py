from django.contrib import admin
from django.urls import path
from . import views # from . 안하면 views 인식 못한다.

urlpatterns = [
    path('main/', views.community_main, name="community_main"),
    path('view/', views.community_view, name="community_view"),
    path('register/', views.community_register, name="community_register"),
    path('detail/', views.community_detail, name="community_detail"),
]