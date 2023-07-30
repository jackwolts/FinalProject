from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username taken")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password)
                user.save()
            print("user created")
        else:
            messages.info(request,"password not matching")
            return redirect('register')
        return redirect('login')

    return render(request, "register.html")

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('my_view')
        else:
            messages.info(request,"invailed credentials")
            return redirect('login')
    return render(request,"login.html")

def home(request):
    return render(request,"home.html")
