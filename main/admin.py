from django.contrib import admin
from .models import Category,Brand,Color,Product



#class ProductAdmin(admin.ModelAdmin):
#    list_display=('id','title','category','brand','status')
    
admin.site.register(Product)


# Register your models here.
