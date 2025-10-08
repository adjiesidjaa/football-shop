from django.urls import path
from main.views import show_main
from .views import (
    product_list, create_product, product_detail,
    product_xml, product_json, product_xml_by_id, product_json_by_id,
    register, login_user, logout_user, edit_product, delete_product,create_car,
    api_products, api_products_create, api_products_update, api_products_delete,
    api_login, api_register, api_logout, api_csrf
)

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('products/', product_list, name='product_list'),
    path('products/create/', create_product, name='create_product'),
    path('car/create/', create_car, name='create_car'),
    path("<int:product_id>/", product_detail, name="product_detail"),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('news/<int:product_id>/edit', edit_product, name='edit_product'),
    path('products/<int:product_id>/delete/', delete_product, name='delete_product'),

    path("xml/", product_xml, name="product_xml"),
    path("json/", product_json, name="product_json"),
    path("xml/<int:product_id>/", product_xml_by_id, name="product_xml_by_id"),
    path("json/<int:product_id>/", product_json_by_id, name="product_json_by_id"),

    # Ajax
    path('api/csrf/', api_csrf, name='api_csrf'),

    path('api/auth/login/', api_login, name='api_login'),
    path('api/auth/register/', api_register, name='api_register'),
    path('api/auth/logout/', api_logout, name='api_logout'),

    path('api/products/', api_products, name='api_products'),
    path('api/products/create/', api_products_create, name='api_products_create'),
    path('api/products/<int:product_id>/update/', api_products_update, name='api_products_update'),
    path('api/products/<int:product_id>/delete/', api_products_delete, name='api_products_delete'),

]