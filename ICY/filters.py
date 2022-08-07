from django_filters import FilterSet
from .models import Product


class CategoryFilter(FilterSet):
    class Meta:
        model = Product
        fields = ['category']
