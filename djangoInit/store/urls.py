from django.urls import path
from .views import category_view, product_view

urlpatterns = [
    path('categories/', category_view, name='category-list'),
    path('products/', product_view, name='product-list'),
]