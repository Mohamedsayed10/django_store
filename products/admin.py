from django.contrib import admin
from . models import products , Category

# Register your models here.
admin.site.register(products)
admin.site.register(Category)