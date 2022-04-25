from django.db import models
from django.shortcuts import render

# IMPORT VIEW 
from django.views.generic import ListView, DetailView

# MODELS 
from App_Shop.models import Product

# MIXIN
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class Home(ListView):
    model = Product
    template_name = 'App_Shop/home.html'

class ProductDetail(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'App_Shop/product_detail.html'
