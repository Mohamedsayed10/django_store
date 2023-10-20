import os
from django.conf import settings
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from . models import Product,Category
from . forms import Productform
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    products = Product.objects.all()
    context = {
        'products': products}
    return render(request,'products\home.html',context )


def contact(request):
    return render(request,'products\contact.html')
def about (request):
    return render(request,"products\\about.html")

def detail(request, id):
    product = Product.objects.filter(id = id)

    product = list(product)
    if product:
        print(product[0])
        return render(request,"products\detail.html",{'product':product[0]})

    return HttpResponse("Sorry target product profile not found ")
    

def search(request):
    query = request.GET.get('query')
    products = Product.objects.filter(title__icontains=query)
    context = {
        'products': products,
        'query': query
    }
    return render(request, 'products/search.html', context)    
@login_required
def add_product(request):
    if request.method == 'POST':
        form = Productform(request.POST, request.FILES)
        if form.is_valid():
            if Product.objects.filter(title=form.cleaned_data['title']).exists():
                form.add_error('title', 'A product with this title already exists.')
            else:
            # Save the form data to create a new product object
                product = Product(
                    title=form.cleaned_data['title'],
                    image=form.cleaned_data['image'],
                    price=form.cleaned_data['price'],
                    description=form.cleaned_data['description'],
                    category=form.cleaned_data['category'],
                    owner=request.user
                )
                product.save()
                return redirect('home')
    else:
        form = Productform()

    context = {
        'form': form
    }
    return render(request, 'products/add_product.html', context)

@login_required
def edit_product(request, id):
    product = get_object_or_404(Product, id=id)
    
    if product.owner != request.user:
        return HttpResponse("You are not authorized to edit this product.")

    if request.method == 'POST':
        form = Productform(request.POST, request.FILES)
        if form.is_valid():
            product.title = form.cleaned_data['title']
            product.price = form.cleaned_data['price']
            product.description = form.cleaned_data['description']
            product.category = form.cleaned_data['category']

            # Check if a new image is provided
            if 'image' in request.FILES:
                product.image = form.cleaned_data['image']
            

            product.save()
            return redirect('home')
    else:
        form = Productform({
            'title': product.title,
            'price': product.price,
            'description': product.description,
            'category': product.category,
            }
        )

    context = {
        'form': form
    }
    return render(request, 'products/edit_product.html', context)

@login_required
def delete(request, id):
    product = get_object_or_404(Product, id=id)
    # product = Product.objects.filter(id=id)
    if product.owner != request.user:
        return HttpResponse("You are not authorized to delete this product.")
    
    if product:
        product_instance = product
        image_path = product_instance.image.path
        if os.path.exists(image_path):
            os.remove(image_path)

        product_instance.delete()
        print(request.user,'I am delete function in views.py')
        return redirect('home')
    else:
        return HttpResponse("Sorry, product not found")    
    
def category_list(request):
    categories = Category.objects.all()
    context = {
        'categories': categories}
    return render(request,'products\category.html',context )

def category_detail(request, category):
    products = Product.objects.filter(category__name=category)
    context = {
        'products': products,
        'category': category
    }
    return render(request, 'products/category_detail.html', context)
