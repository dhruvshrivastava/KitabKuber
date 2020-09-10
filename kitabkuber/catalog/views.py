from django.shortcuts import render
from django.views.generic import ListView
from catalog.models import Books, Orders
from .forms import RentForm
from django.http import HttpResponse
import uuid

class Home(ListView):
    model = Books
    template_name = 'catalog/home.html'

def bookdetail(request,id):
     book = Books.objects.get(pk=id)
     return render(request, 'catalog/book.html', {'book':book})

def checkout(request, id):
    product = Books.objects.get(pk=id)
    if request.method == 'POST':
        rental = request.POST.get('rental')
    return render(request, 'catalog/checkout.htm', {'product':product, 'rental': rental})

def order(request, id):
    if request.method == 'POST':
       book_ordered = Books.objects.get(pk=id)
       name = request.POST.get('name', False)
       email = request.POST.get('email', False)
       line1 = request.POST.get('line1', False)
       line2 = request.POST.get('line2', False)
       pincode = request.POST.get('pincode', False)
       city = request.POST.get('city', False)
       mobile = request.POST.get('mobile', False)
       rental = request.POST.get('rental', False)
       order_reference = uuid.uuid1()
       data = {
        'reference_number': order_reference,
        'book_ordered': book_ordered,
        'name': name,
        'email': email,
        'address_line_1': line1,
        'address_line_2': line2,
        'pincode': pincode,
        'city': city,
        'mobile': mobile,
        'rental': rental
         }
       order_instance = Orders.objects.create(customer_name = name,
        customer_email = email,
        customer_mobile = mobile,
        book_ordered = book_ordered,
        customer_city = city,
        customer_pincode = pincode,
        customer_line1 = line1,
        customer_line2 = line2,
        order_number= order_reference,
        rental = rental)
    else: 
        return HttpResponse('Please place an order first')
    return render(request, 'catalog/thanks.html', {'data': data})

     

