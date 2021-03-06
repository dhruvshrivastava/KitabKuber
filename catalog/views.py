from django.shortcuts import render
from django.views.generic import ListView
from catalog.models import Books, Orders, Sell, Enquiry
from .forms import RentForm
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
import uuid
from django.core.mail import BadHeaderError
from django.core import mail



class Home(ListView):
    model = Books
    template_name = 'catalog/home.html'

def bookdetail(request,id):
     categories = []
     book = Books.objects.get(pk=id)
     category = book.book_category
     other_books = Books.objects.exclude(id=id)
     for books in other_books: 
        if books.book_category == category:
            categories.append(books)
     
     return render(request, 'catalog/book.html', {'book':book, 'categories': categories})

def checkout(request, id):
    product = Books.objects.get(pk=id)
    if request.method == 'POST':
        rentalperiod = request.POST.get('rentalperiod')
        request.session['rentalperiod'] = rentalperiod
    return render(request, 'catalog/checkout.htm', {'product':product, 'rentalperiod': rentalperiod})

def rental(request, id):
    product = Books.objects.get(pk=id)
    return render(request, 'catalog/rental.html', {'product':product})

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
       order_reference = uuid.uuid1()
       rentalperiod = request.session['rentalperiod']
       
       data = {
        'deductible': '0',
        'rentalperiod': rentalperiod,
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
        rentalperiod= rentalperiod,
        deductible='0')
    else: 
        return HttpResponse('Please place an order first')
    return render(request, 'catalog/thanks.html', {'data': data})

def search(request):
    try:
     if request.method == 'POST':
        name = request.POST.get('search', False)
        search_results = Books.objects.filter(book_name__search = name)
     return render(request, 'catalog/search.html', {'search_results': search_results})
    except:
        return render(request, 'catalog/home.html')

def categories(request):
    if request.method == 'POST':
        category = request.POST.get('categories')
        search_category = Books.objects.filter(book_category=category)
    return render(request, 'catalog/categories.html', {'search_category': search_category})
     

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        message = request.POST.get('message')
        if message and email:
            try: 
                connection = mail.get_connection()
                connection.open()
                email1 = mail.EmailMessage(
                    'enquiry',
                    message,
                    email,
                    ['dhruvsri5@gmail.com'],
                    connection=connection
                )
                email1.send()
                connection.close()
            except BadHeaderError:
                return HttpResponse("Invalid Header Found")
            return HttpResponse('Your response has been recieved, we will contact you shortly')
        else:
            return HttpResponse('Make sure all fields are entered and are valid')

    return render(request, 'catalog/contact.html')

def sell(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        bookname = request.POST.get('bookname')
        bookpublisher = request.POST.get('bookpublisher')
        book_image = request.FILES['file']
        sell_enquiry = Sell.objects.create(name = name,
        email = email,
        mobile = mobile,
        bookname = bookname,
        bookpublisher = bookpublisher,
        book_image = book_image
        )
        if (sell_enquiry):
         return HttpResponse('Your enquiry has been generated successfully! We will contact you shortly')

    return render(request, 'catalog/sell.html')

def faq(request):
    return render(request, 'catalog/faq.html')

def enquiry(request):
  try: 
      if request.method == 'POST':
          name = request.POST.get('name')
          mobile = request.POST.get('mobile')
          email = request.POST.get('email')
          book_name = request.POST.get('book_name')
          book_author = request.POST.get('author')
          enquiry_instance = Enquiry.objects.create(book_name=book_name, book_author=book_author, name=name, email=email, mobile=mobile)
          return HttpResponse("Thank you for filling the form! We will get back to you with more details in 24 hours.")
  except:
      return render(request, 'catalog/home.html')