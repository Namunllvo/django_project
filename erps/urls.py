# tweet/urls.py
from django.urls import path
from erps import views

urlpatterns = [
    path('', views.home, name='home'),  # 127.0.0.1:8000 과 views.py 폴더의 home 함수 연결
    path('erps/create/', views.product_create, name='product_create'),   # 127.0.0.1:8000/erps 과 views.py 폴더의 product_create 함수 연결
    path('erps/list/', views.product_list, name='product_list'),  # 127.0.0.1:8000/erps 과 views.py 폴더의 product_list 함수 연결
    # path('erps/in_c/', views.inbound_create, name='inbound_create'),
    path('erps/stock/', views.inventory, name='inventory'),
]
