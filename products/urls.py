
from django.urls import path
from . views import home,contact,about,detail,delete,search,add_product,edit_product,category_list,category_detail

urlpatterns = [

    path('', home,name="home"),
    path('detail/<int:id>', detail,name="detail"),
    path('delete/<int:id>', delete,name="delete"),
    path('about', about,name="about"),
    path('contact', contact,name="contact"),
    path('search', search, name="search"),
    path('add_product/', add_product, name='add_product'),
    path('edit_product/<int:id>/', edit_product, name='edit_product'),
    path('category_list',category_list,name='category_list'),
    path('category/<str:category>/', category_detail, name='category_detail'),
]
