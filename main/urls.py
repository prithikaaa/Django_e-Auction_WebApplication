from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

from register import views as v
urlpatterns = [
    
    path('', views.homePage,name='home'),
    path('search',views.search,name='search'),
    path('about-us/',views.aboutUs),
   # path('log-in/',views.login),
    path('category-list/',views.category_list,name='category-list'),
    path('category-product-list/<int:cat_id>',views.category_product_list,name='category-product-list'),
    
    path('register/',v.register,name="signup"),
    path('product-details/<int:id>',views.product_detail,name='product_detail')
    ]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)