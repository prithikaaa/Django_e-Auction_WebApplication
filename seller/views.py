from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from main.models import Category,Product
from main.forms import SignupForm
from .forms import SellerForm
def homePage(request):
    
    return render(request,"index.html", {'navbar':'Home'})
'''def aboutUs(request):
     return render(request,"aboutus.html", {'navbar':'About Us'})
def login(request):
    return render(request,"registration/login.html", {'navbar':'Login'})
def register(response):
   if response.method == "POST":
       form=SignupForm(response.POST)
       if form.is_valid():
           form.save()
       return redirect("/visit/create")
   else:
       form=SignupForm()
   return render(response,"register.html",{"form":form})'''
def showformdata(request):
    fm = SellerForm()
    return render(request,"registration.html", {"form":fm})
def product_detail(request,id):
     obj=Product.objects.get(id=id)
     return render(request,'product.html',{"obj":obj})

# Create your views here.

# Create your views here.
