# from django.shortcuts import get_object_or_404
from . models import Product
from . serializers import ProductSerializer
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
from rest_framework import generics




# Generic Views
class ProductListApi(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
class ProductDetailApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'  