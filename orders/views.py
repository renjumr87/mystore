from django.shortcuts import render

# Cart
def show_cart(request):
    return render(request, 'cart.html')
