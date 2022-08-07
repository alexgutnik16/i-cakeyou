from email.policy import default
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Product, Images
from .filters import CategoryFilter


class ProductsView(ListView):
    template_name = 'index.html'
    context_object_name = 'products'
    queryset = Product.objects.all()
    images = Images.objects.filter(default=True)

    def get_filter(self):
        return CategoryFilter(self.request.GET, queryset=super().get_queryset())

    def get_queryset(self):
        return self.get_filter().qs

    def get_context_data(self, *args, **kwargs):
        return {
            **super().get_context_data(*args, **kwargs),
            'filter': self.get_filter(),
            'images': self.images
        }


class ProductView(DetailView):
    queryset = Product.objects.all()
    template_name = 'product.html'

    def get_context_data(self, **kwargs):
        context = super(ProductView, self).get_context_data(**kwargs)
        context['images'] = Images.objects.all()
        return context
