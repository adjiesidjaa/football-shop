from django.shortcuts import render
from .models import Product

def show_main(request):
    context = {
        "app_name": "Sidja",
        "student_name": "Adjie M. Usman",
        "student_class": "PBP C",
    }
    return render(request, "main.html", context)

def product_list(request):
    products = Product.objects.all()
    return render(request, "product_list.html", {"products": products})
