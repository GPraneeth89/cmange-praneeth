from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def Home(request):
    
    return render(request,'crm/dashboard.html')
def products(request):
    return render(request,'crm/products.html')
def customer(request):
    return render(request,'crm/customer.html')