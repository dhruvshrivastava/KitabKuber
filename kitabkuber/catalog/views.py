from django.shortcuts import render
from django.views.generic import ListView
from catalog.models import Books

class Home(ListView):
    model = Books
    template_name = 'catalog/home.html'