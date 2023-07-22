from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from main.forms import SignupForm

def homePage(request):
    
    return render(request,"index.html", {'navbar':'Home'})
def aboutUs(request):
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
   return render(response,"register.html",{"form":form})

# Create your views here.
