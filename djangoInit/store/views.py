from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def product_list(request):
    return HttpResponse("Product list view")

def product_cost(request):
    return HttpResponse("Product cost view")



