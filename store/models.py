from django.db import models
from category.models import category
# Create your models here.
from django.urls import reverse
class Product(models.Model):
    product_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    description = models.TextField(max_length=255,blank=True)
    price = models.IntegerField()
    images=models.ImageField(upload_to='photos/products')
    stock = models.IntegerField()
    is_avilable =models.BooleanField(default=True)
    category =models.ForeignKey(category,on_delete=models.CASCADE)

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date=models.DateTimeField(auto_now=True)
    
    def get_url(self):
        return reverse ('product_details',args =[self.category.slug,self.slug])



    def __str__(self):
        return self.product_name