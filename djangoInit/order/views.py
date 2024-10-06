from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def order_list(request):
    return HttpResponse("Order list view")

def order_detail(request):
    return HttpResponse("Order detail view")

