from django.urls import path 
from .views import Home, bookdetail, order, search, categories, rental, contact, checkout
from django.conf.urls.static import static
from django.conf import settings 

urlpatterns = [

    path('', Home.as_view(), name = 'home'),
    path('book/<int:id>/', bookdetail, name = 'bookdetail'),
    path('book/<int:id>/rental/', rental, name = 'rental'),
    path('book/<int:id>/rental/checkout/', checkout, name = 'checkout'),
    path('book/<int:id>/rental/checkout/order/', order, name='order'),
    path('search/', search, name = 'search'),
    path('categories/', categories, name='categories'),
    path('contact/', contact, name='contact')
]  