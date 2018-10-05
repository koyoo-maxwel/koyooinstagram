from django.shortcuts import render

# Create your views here.

from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404
from .models import Profile,User,Image






@login_required(login_url='/accounts/login/')
def home(request):
    image = Image.objects.all()
    return render(request,'all-images/home.html',{'images':image})


def profile(request):
    profile = Profile.objects.filter(user=profile)
    return render(request,'all-images/profile.html',{'profile':profile})



