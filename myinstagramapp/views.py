from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404
from .models import Profile,User,Image

# Create your views here.

def home(request):
    image = Image.objects.all()
    return render(request,'all-images/home.html',{'image':image})
