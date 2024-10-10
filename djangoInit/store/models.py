from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="სახელი")
    description = models.TextField(verbose_name="აღწერა", blank=True, null=True)
    parent = models.ForeignKey('self', blank =True, null = True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="სახელი")
    description = models.TextField(verbose_name="აღწერა", blank = True, null = True)
    categories = models.ManyToManyField(Category, related_name='products')
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to = "products/", null = True, blank = True)
    
    
    def __str__(self):
        return self.name
    
    
