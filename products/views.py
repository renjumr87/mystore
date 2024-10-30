from django.shortcuts import render
from . models import Product
from django.core.paginator import Paginator
# Create your views here.
def index(request):
    return render(request,'index.html')
    
# List Products
def list_products(request):
    """_summary_"""
    page=1
    if request.GET:
        page=request.GET.get('page',1)
    product_list=Product.objects.all()
    product_paginator=Paginator(product_list,2)
    product_list=product_paginator.get_page(page)
    context={'products':product_list}
    return render(request, 'products.html',context)

# Product Details
def detail_products(request):
    return render(request, 'prducts_details.html')
