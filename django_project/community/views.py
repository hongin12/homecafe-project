from django.shortcuts import render
from django.shortcuts import get_object_or_404

# Create your views here.

def community_main(request):
    return render(request, "community_main.html")

def community_view(request):
    return render(request, "community_view.html")

def community_register(request):
    return render(request, "community_register.html")

def community_detail(request):
    return render(request, "community_detail.html")