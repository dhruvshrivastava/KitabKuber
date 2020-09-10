from django.urls import path 
from .views import Home, bookdetail, checkout, order
from django.conf.urls.static import static
from django.conf import settings 

urlpatterns = [

    path('', Home.as_view(), name = 'home'),
    path('book/<int:id>/', bookdetail, name = 'bookdetail'),
    path('book/<int:id>/checkout/', checkout, name = 'checkout'),
    path('book/<int:id>/checkout/order/', order, name = 'order')
]  