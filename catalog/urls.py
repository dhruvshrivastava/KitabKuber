from django.urls import path 
from .views import Home, bookdetail, sell, order, search, categories, rental, contact, checkout, faq
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
    path('contact/', contact, name='contact'),
    path('sell/', sell, name = 'sell'),
    path('faq/', faq, name = 'faq'),

]  