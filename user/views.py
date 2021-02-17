from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import Register,Login
from django.contrib.auth import login,authenticate,logout
# Create your views here.

def index(request):
    return render(request,"index.html")

def register(request):
    form = Register(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")  
        newUser = User(username = username)
        newUser.set_password(password)
        newUser.save()
        login(request,newUser)
        messages.success(request, "User registered successfully ...")
        return redirect("todo:dashboard")
    return render(request,"register.html",{"form":form})

def loginUser(request):
    form = Login(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username = username,password = password)
        if user:
            login(request,user)
            messages.success(request,"User login successfully ...")
            return redirect("todo:dashboard")
        else:
            messages.warning(request,"Username or password is wrong !!!")
            return render(request,"login.html",{"form":form})
    return render(request,"login.html",{"form":form})

def logoutUser(request):
    logout(request)
    messages.warning(request,"User logout successfully ...")
    return redirect("index")



