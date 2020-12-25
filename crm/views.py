from django.shortcuts import render,redirect
from .models import *
from .forms import *
# Create your views here.
from django.http import HttpResponse

def Home(request):
    orders=Order.objects.all()
    customer=Customer.objects.all()
    total_customers=customer.count()
    total_orders=orders.count()
    orders_delivered=orders.filter(status='Delivered').count()
    orders_pending=orders.filter(status='Pending').count()
    out_for=orders.filter(status='Out for Delivery').count()

    context={'orders':orders,
    'customer':customer,
    'total_orders':total_orders,
    'orders_delivered':orders_delivered,
    'orders_pending' : orders_pending,
    'out_for':out_for
    }
    
    return render(request,'crm/dashboard.html',context)
def products(request):
    products=Product.objects.all()
    return render(request,'crm/products.html',{'products':products})
def customer(request,pk):
    customer=Customer.objects.get(id=pk)
    
    orders=customer.order_set.all()
    orders_count=orders.count()
    context={'customer':customer,'orders':orders,'oc':orders_count}
    return render(request,'crm/customer.html',context)

def createOrder(request):
    forms=OrderForm()
    if request.method=='POST':
        # print('Printing POST' , request.POST)
        forms=OrderForm(request.POST)
        if forms.is_valid:
            forms.save()
            return redirect('/')
    context={'forms':forms}
    return render(request,'crm/order_form.html',context)

def UpdateOrder(request,pk):
    order=Order.objects.get(id=pk)

    forms=OrderForm(instance=order)
    if request.method=='POST':
        forms=OrderForm(request.POST,instance=order)
        if forms.is_valid:
            forms.save()
            return redirect('/')
    context={'forms':forms}
    return render(request,'crm/order_form.html',context)

def DeleteOrder(request,pk):
    order=Order.objects.get(id=pk)
    if request.method=='POST':
        order.delete()
        return redirect('/')


    context={'item':order}
    return render(request,"crm/delete_order.html",context)