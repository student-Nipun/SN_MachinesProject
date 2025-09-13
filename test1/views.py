from django.shortcuts import render, HttpResponse, redirect
from .models import Contact_Query, Products
from django.db.models import Q

# Create your views here.
def home(request):
    return render(request,'test1/home.html')

def findProduct(request):
    if request.method == 'POST':
        x = request.POST.get('prod_search')
        mydata = Products.objects.filter(Q(product_name__icontains = x))
        if mydata:
            return render(request,'test1/products.html', {'product_info':mydata})
        else:
            return render(request,'test1/products.html', {'warning':'No Record Found'})


def about(request):
    return render(request,'test1/about.html')

def products(request):
    product_info = Products.objects.all()
    print(product_info)
    return render(request,'test1/products.html',{'product_info':product_info})

def contact(request):
    return render(request,'test1/contact.html')
    