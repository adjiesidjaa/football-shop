from django.urls import path
from main.views import show_main
from .views import (
    product_list, create_product, product_detail,
    product_xml, product_json, product_xml_by_id, product_json_by_id,
    register, login_user, logout_user, edit_product, delete_product
)

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('products/', product_list, name='product_list'),
    path('products/create/', create_product, name='create_product'),
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
]