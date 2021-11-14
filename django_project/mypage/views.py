from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import auth 
from django.contrib.auth.models import User

def mypage_main(request):
    return render(request, "mypage_main.html")

def mypage_edit_profile(request):
    return render(request, 'mypage_edit_profile.html')

def mypage_like_recipes(request):
    return render(request, 'mypage_like_recipes.html')

def mypage_my_comment(request):
    return render(request, "mypage_my_comment.html")

def mypage_my_follow(request):
    return render(request, "mypage_my_follow.html")

def mypage_my_recipes(request):
    return render(request, "mypage_my_recipes.html")

