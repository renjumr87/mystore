from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')
    
# List Products
def list_products(request):
    """_summary_"""
    return render(request, 'products.html')

# Product Details
def detail_products(request):
    return render(request, 'prducts.html')