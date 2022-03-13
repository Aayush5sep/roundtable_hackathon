from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import Orders,UserDetails
from affiliates.models import ProductLinks


# Create your views here.
def signuppage(request):
    return render(request,'signup.html')

def signup(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        email=request.POST['email']
        fname=request.POST['fname']
        lname=request.POST['lname']
        phone=request.POST['phone']

        newuser=User.objects.create_user(username,email,password)
        user=authenticate(username=username,password=password)
        login(request,user)
        userd=UserDetails(user=user,fname=fname,lname=lname,phone=phone)
        userd.save()
        messages.success(request,"User Account Created Successfully")
        return render(request,'homepage.html')
    else:
        return HttpResponse("Creating new user account failed !")

def loginpage(request):
    return render(request,'login.html')

def loginn(request):
    if request.method=='POST':
        login_username=request.POST['username']
        login_password=request.POST['password']

        user=authenticate(username=login_username,password=login_password)
        if user is not None:
            login(request,user)
            messages.success(request,'Login Successful')
            return render(request,'homepage.html')
        else:
            messages.error(request,'Login Failed')
            return HttpResponse("Oops! Login Failed")
    else:
        return HttpResponse("Unsecured Login Error !!")

def logot(request):
    logout(request)
    messages.success(request,'Logout Successful')
    return render(request,'homepage.html')

def dashboard(request):
    user=request.user
    ordered=Orders.objects.filter(user=user)
    userd=UserDetails.objects.filter(user=user)
    orders=[]
    for order in ordered:
        prods=order.product_id
        orders.append(prods)
    return render(request,'dashboard.html',{'ordered':orders,'userd':userd})