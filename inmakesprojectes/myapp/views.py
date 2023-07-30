from django.contrib import auth
from django.contrib.auth.models import User
from django.http import JsonResponse
from .models import Subcategory
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Category, Subcategory




def submit_form(request):
    if request.method == 'POST':
        message = "Order Confirmed"
        return render(request, "home.html", {'message': message})

    return render(request, "home.html")

def form(request):
    if request.method == 'POST':
        first_name=request.POST['first_name']
        email=request.POST['email']
        user=User.objects.create_user(first_name=first_name,email=email)

        user.save()


def demo(request):
    return render(request,"index.html")


def my_view(request):
    categories = Category.objects.all()
    return render(request, 'my_template.html', {'categories': categories})


def get_subcategories(request):
      category_id = request.GET.get('category_id')
      subcategories = Subcategory.objects.filter(category_id=category_id).values('id', 'name')
      return JsonResponse(list(subcategories), safe=False)


def home(request):
    return render(request, 'home.html')


