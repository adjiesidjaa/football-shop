from .models import Product
from django.shortcuts import render, redirect,get_object_or_404
from .forms import ProductForm
from django.http import HttpResponse
from django.core import serializers


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

def create_product(request):
    form = ProductForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("main:product_list")
    return render(request, "create_product.html", {"form": form})

def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, "product_detail.html", {"product": product})

def product_xml(request):
    products = Product.objects.all()
    xml_data = serializers.serialize("xml", products)
    return HttpResponse(xml_data, content_type="application/xml")

def product_json(request):
    products = Product.objects.all()
    json_data = serializers.serialize("json", products)
    return HttpResponse(json_data, content_type="application/json")

def product_xml_by_id(request, product_id):
    try:
        product = Product.objects.filter(pk=product_id)
        xml_data = serializers.serialize("xml", product)
        return HttpResponse(xml_data, content_type="application/xml")
    except Product.DoesNotExist:
        return HttpResponse(status=404)

def product_json_by_id(request, product_id):
    try:
        product = Product.objects.get(pk=product_id)
        json_data = serializers.serialize("json", [product])
        return HttpResponse(json_data, content_type="application/json")
    except Product.DoesNotExist:
        return HttpResponse(status=404)
