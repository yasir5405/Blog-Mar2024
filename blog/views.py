from django.shortcuts import render, HttpResponse, redirect
from .models import Blog
from datetime import datetime
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db import IntegrityError
# Create your views here.
def home(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return redirect('landingpage')
    else:
        return render(request, 'landingpage.html')
def register(request):
    if request.method == "POST":
        if request.POST.get('password')==request.POST.get('password1'):
            username = request.POST.get('username')
            password = request.POST.get('password')
            try:
                saveuser = User.objects.create_user(username, password)
                saveuser.set_password(password)
                saveuser.save()
                messages.success(request, "Account created successfully")
                return redirect('landingpage')
            except IntegrityError:
                messages.error(request, "Username already exists!")
                return render(request, 'register.html')
        else:
            return render(request, 'register.html')
    else:
        return render(request, 'register.html')
def logOut(request):
    if request.method == "POST":
        logout(request)
        messages.success(request, 'You have been successfully logged out')
        return redirect('landingpage')
def index(request):
    blogs = Blog.objects.all()
    context = {
        'blogs' : blogs,
    }
    return render(request, 'home.html', context)
def post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        name = request.POST.get('name')
        description = request.POST.get('desc')
        blog = Blog(title=title, name = name, desciption = description, date = datetime.today())
        blog.save()
        messages.success(request, "Your blog has been posted successfully")
        return render(request, 'form.html')
    else:
        return render(request, 'form.html')
