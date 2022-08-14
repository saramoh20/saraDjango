from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from .models import *


def dashboard(request):
    customers = Customer.objects.all()
    orders = Order.objects.all()
    t_orders = orders.count()
    p_orders = orders.filter(status='pending').count()
    d_orders = orders.filter(status='Delivered').count()
    in_orders = orders.filter(status='in progress').count()
    out_orders = orders.filter(status='').count()
    context = {'customers': customers,
               'orders': orders,
               't_rders': t_orders,
               'p_orders': p_orders,
               'd_orders': d_orders,
               'in_orders': in_orders,
               'out_orders': out_orders}
    return render(request, 'bookstore/dashboard.html', context)


def books(request):
    books = Book.objects.all()
    return render(request, 'bookstore/books.html', {'book': books})


def customer(request, pk):
    customer = Customer.objects.get(id=pk)
    return render(request, 'bookstore/customer.html')
