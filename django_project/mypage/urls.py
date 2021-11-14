from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('mypageMain/', views.mypage_main, name = 'mypage_main'),
    path('myComment/', views.mypage_my_comment, name="my_comment"),
    path('myRecipes/', views.mypage_my_recipes, name="my_recipes"),
    path('myFollow/', views.mypage_my_follow, name="my_follow"),
    path('likeRecipes/', views.mypage_like_recipes, name="like_recipes"),
    path('editProfile/', views.mypage_edit_profile, name="edit_profile"),
]