from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    return render(request,'landpage.html')

def contact(request):
    return render(request,'contactus.html')

