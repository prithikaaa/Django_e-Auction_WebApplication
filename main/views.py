from django.shortcuts import render,redirect
from .models import Category,Product
from django.contrib.auth.forms import UserCreationForm
from .forms import SignupForm

# home
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
   return render(response,"register/register.html",{"form":form})
def product_detail(request,id):
     obj=Product.objects.get(id=id)
     return render(request,'product.html',{"obj":obj})
#category
def category_list(request):
    data=Category.objects.all().order_by('-id')
    return render(request,"category_list.html",{"data":'data'})
# Product List According to Category
def category_product_list(request,cat_id):
	category=Category.objects.get(id=cat_id)
	data=Product.objects.filter(category=category).order_by('-id')
	return render(request,'category_product_list.html',{
			"data":'data',
			})
# Search
def search(request):
	q=request.GET['q']
	data=Product.objects.filter(title__icontains=q).order_by('-id')
	return render(request,'search.html',{"data":'data'})
