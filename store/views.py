from django.shortcuts import render,get_object_or_404
from .models import Product
from category.models import category
# Create your views here.
def store(request,category_slug=None):
    categories =None
    products=None
    if category_slug!=None:
        categories=get_object_or_404(category,slug=category_slug)
        products=Product.objects.filter(category=categories,is_avilable=True)
        product_count=products.count()
    else:


        products=Product.objects.all().filter(is_avilable=True)
        product_count = products.count()
    context ={

        "products": products,
        "product_count": product_count,
        }
    return render(request,'store/store.html',context)


def product_details(request,category_slug,product_slug):
    try:
        single_product=Product.objects.get(category__slug=category_slug,slug=product_slug)
    except Exception as e:
        raise e  

    context ={
        "single_product": single_product
    }

    return render(request,'store/product_details.html',context)
