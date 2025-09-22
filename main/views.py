from .models import Product
from django.shortcuts import render, redirect,get_object_or_404
from .forms import ProductForm
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import datetime



@login_required(login_url='/login')
def show_main(request):
    context = {
        "app_name": "Sidja",
        "student_name": "Adjie M. Usman",
        "student_class": "PBP C",
        "last_login": request.COOKIES.get('last_login', 'Never')
    }
    return render(request, "main.html", context)

@login_required(login_url='/login')
def product_list(request):
    filter_type = request.GET.get("filter", "all")

    if filter_type == "all":
        products = Product.objects.all()
    else:
        products = Product.objects.filter(user=request.user)

    return render(request, "product_list.html", {
        "products": products,
        "filter_type": filter_type,
    })


@login_required(login_url='/login')
def create_product(request):
    form = ProductForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user   # hubungkan produk dengan user yang sedang login
            product.save()
            return redirect("main:product_list")
        else:
            messages.error(request, "Data produk tidak valid. Mohon periksa kembali.")

    return render(request, "create_product.html", {"form": form})

@login_required(login_url='/login')
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
    
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
    else:
        form = AuthenticationForm(request)
    context = {'form': form}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    return redirect('main:login')


