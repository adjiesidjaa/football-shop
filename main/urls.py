from django.urls import path
from main.views import show_main
from .views import show_main, product_list

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('products/', product_list, name='product_list')
]