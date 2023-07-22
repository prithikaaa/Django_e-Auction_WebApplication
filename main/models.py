from django.db import models
class Category(models.Model):
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to="cat_imgs/")


    def __str__(self):
        return self.title
    #brand
class Brand(models.Model):
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to="brand_imgs/")


    def __str__(self):
        return self.title
    #colour
class Color(models.Model):
    title=models.CharField(max_length=100)
    color_code=models.CharField(max_length=100)


    def __str__(self):
        return self.title
    # Product Model
class Product(models.Model):
    title=models.CharField(max_length=200)
    image=models.ImageField(upload_to="product_imgs/")
    slug=models.CharField(max_length=400)
    detail=models.TextField()
    specs=models.TextField()
    
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE)
    
    status=models.BooleanField(default=True)
    

    def __str__(self):
        return self.title

