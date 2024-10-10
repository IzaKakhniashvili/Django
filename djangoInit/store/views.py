from django.shortcuts import render
from django.http import JsonResponse
from .models import Category, Product


def category_view(request):
    categories = Category.objects.filter(parent=None)
    category_list = [
        {
            'id': category.id,
            'name': category.name,
            'description': category.description,
            'children': [
                {'id': child.id, 'name': child.name, 'description': child.description}
                for child in Category.objects.filter(parent=category)
            ]
        }
        for category in categories
    ]
    
    return JsonResponse(category_list, safe=False)

def product_view(request):
    products = Product.objects.all()
    product_list = [
        {
            'id': product.id,
            'name': product.name,
            'description': product.description,
            'price': product.price,
            'image': product.image.url if product.image else None, 
            'categories': [
                {'id': category.id, 'name': category.name, 'description': category.description}
                for category in product.categories.all()
            ]
        }
        for product in products
    ]
    return JsonResponse(product_list, safe=False)



