from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404
from .models import Profile,Comment,User

# Create your views here.

def home(request):
    user = User.objects.all()
    return render(request,'all-images/home.html',{'user':user})
