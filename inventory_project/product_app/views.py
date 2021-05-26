#-------------Imports-------------------------------------------
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from productapp.forms import ProductForm
from productapp.models import Product

#-------------Views---------------------------------------------
class ProductList(ListView):
    template_name = 'pages/products.html'
    model = Product
    context_object_name= 'products'

class ProductDetail(DetailView):
    model = Product
    template_name = 'pages/product_details.html'
    context_object_name = 'product'


class ProductNew(LoginRequiredMixin,CreateView):
    model = Product
    fields = '__all__'
    exclude = ['user']
    template_name = 'pages/new_product.html'
    success_url = reverse_lazy('product:product_list')
    login_url= 'login'

    def form_valid(self, form):
        form.instance.user = self.request.user 
        return super(ProductNew, self).form_valid(form)

class ProductUpdate(UpdateView):
    model = Product
    fields = '__all__'
    exclude = ['user']
    template_name = 'pages/product_update.html'
    success_url = reverse_lazy('product:product_list')


class ProductDelete(DeleteView):
    model = Product
    template_name = 'productapp/product_delete.html'
    context_object_name = 'product'
    success_url = reverse_lazy('product:product_list')
