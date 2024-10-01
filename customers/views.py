from django.shortcuts import render

# Account
def show_account(request):
    return render(request, 'account.html')