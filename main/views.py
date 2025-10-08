from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.core import serializers
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.http import require_http_methods
from django.middleware.csrf import get_token
from django.contrib import messages
import datetime

from .models import Product
from .forms import ProductForm, CarForm


@login_required(login_url='/login')
def show_main(request):
    context = {
        "app_name": "Sidja",
        "student_name": "Adjie M. Usman",
        "student_class": "PBP C",
        "student_npm": "2406423313",
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
def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, "product_detail.html", {"product": product})


@login_required(login_url='/login')
def create_product(request):
    form = ProductForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        product = form.save(commit=False)
        product.user = request.user
        product.save()
        messages.success(request, "Produk berhasil ditambahkan!")
        return redirect("main:product_list")
    return render(request, "create_product.html", {"form": form})


@login_required(login_url='/login')
def edit_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    form = ProductForm(request.POST or None, instance=product)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Produk berhasil diperbarui!")
        return redirect("main:product_list")
    return render(request, "edit_product.html", {"form": form, "product": product})


@login_required(login_url='/login')
def delete_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id, user=request.user)
    product.delete()
    messages.success(request, "Produk berhasil dihapus.")
    return HttpResponseRedirect(reverse("main:product_list"))

def register(request):
    """REGISTER normal page (with form)"""
    form = UserCreationForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Akun kamu berhasil dibuat! Silakan login.")
        return redirect("main:login")

    return render(request, "register.html", {"form": form})


def login_user(request):
    """LOGIN normal page (render form + handle fallback POST)"""
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(request.GET.get("next", reverse("main:show_main")))
            response.set_cookie("last_login", str(datetime.datetime.now()))
            return response
        else:
            messages.error(request, "Username atau password salah.")
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form})


def logout_user(request):
    logout(request)
    response = redirect("main:login")
    response.delete_cookie("last_login")
    return response

def product_to_dict(p):
    return {
        "id": p.id,
        "name": p.name,
        "description": p.description,
        "price": p.price,
        "category": p.get_category_display() if hasattr(p, "get_category_display") else p.category,
        "thumbnail": p.thumbnail,
        "is_featured": p.is_featured,
        "stock": p.stock,
        "brand": p.brand,
        "author": p.user.username if p.user else "Anonymous",
    }


@login_required(login_url="/login")
def api_products(request):
    """GET all products"""
    f = request.GET.get("filter", "all")
    qs = Product.objects.all() if f == "all" else Product.objects.filter(user=request.user)
    data = [product_to_dict(p) for p in qs.order_by("-id")]
    return JsonResponse({"ok": True, "items": data, "count": len(data)})


@login_required(login_url="/login")
@require_http_methods(["POST"])
def api_products_create(request):
    form = ProductForm(request.POST)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        return JsonResponse({"ok": True, "item": product_to_dict(obj), "msg": "Produk berhasil dibuat"})
    return JsonResponse({"ok": False, "errors": form.errors}, status=400)


@login_required(login_url="/login")
@require_http_methods(["POST"])
def api_products_update(request, product_id):
    obj = get_object_or_404(Product, pk=product_id)
    if obj.user != request.user:
        return JsonResponse({"ok": False, "msg": "Akses ditolak"}, status=403)
    form = ProductForm(request.POST, instance=obj)
    if form.is_valid():
        obj = form.save()
        return JsonResponse({"ok": True, "item": product_to_dict(obj), "msg": "Produk diperbarui"})
    return JsonResponse({"ok": False, "errors": form.errors}, status=400)


@login_required(login_url="/login")
@require_http_methods(["POST", "DELETE"])
def api_products_delete(request, product_id):
    obj = get_object_or_404(Product, pk=product_id)
    if obj.user != request.user:
        return JsonResponse({"ok": False, "msg": "Akses ditolak"}, status=403)
    obj.delete()
    return JsonResponse({"ok": True, "msg": "Produk dihapus"})


def api_csrf(request):
    """Dapatkan CSRF token"""
    return JsonResponse({"ok": True, "csrfToken": get_token(request)})


@require_http_methods(["POST"])
def api_login(request):
    """AJAX login"""
    form = AuthenticationForm(data=request.POST)
    if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = JsonResponse({"ok": True, "msg": "Login sukses"})
        response.set_cookie("last_login", str(datetime.datetime.now()))
        return response
    return JsonResponse({"ok": False, "errors": form.errors, "msg": "Login gagal"}, status=400)


@require_http_methods(["POST"])
def api_register(request):
    """AJAX register"""
    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        return JsonResponse({"ok": True, "msg": "Registrasi berhasil"})
    return JsonResponse({"ok": False, "errors": form.errors, "msg": "Registrasi gagal"}, status=400)


@login_required(login_url="/login")
@require_http_methods(["POST"])
def api_logout(request):
    """AJAX logout"""
    logout(request)
    return JsonResponse({"ok": True, "msg": "Logout sukses"})

@login_required(login_url="/login")
def create_car(request):
    form_car = CarForm(request.POST or None)
    if request.method == "POST" and form_car.is_valid():
        car = form_car.save(commit=False)
        car.user = request.user
        car.save()
        return redirect("main:car_list")
    return render(request, "create_car.html", {"form": form_car})


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
