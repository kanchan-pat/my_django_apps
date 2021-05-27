#-------------Imports-------------------------------------------
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from product_app.forms import ProductForm
from product_app.models import Product

#-------------Views---------------------------------------------
class ProductList(ListView):
    template_name = 'products.html'
    model = Product
    context_object_name= 'products'

class ProductDetail(DetailView):
    model = Product
    template_name = 'product_details.html'
    context_object_name = 'product'


class ProductNew(LoginRequiredMixin,CreateView):
    model = Product
    fields = '__all__'
    exclude = ['user']
    template_name = 'new_product.html'
    success_url = reverse_lazy('product:products')
    login_url= 'login'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ProductNew, self).form_valid(form)

class ProductUpdate(UpdateView):
    model = Product
    fields = '__all__'
    exclude = ['user']
    template_name = 'product_update.html'
    success_url = reverse_lazy('product:products')
