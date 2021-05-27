#-----------------------Imports-------------------------------
from django.urls import path
from product_app import views

#-----------------------Url Patterns-------------------------------

urlpatterns = [
    path('', views.ProductList.as_view(), name='products'),
    path('products/<int:product_id>/', views.ProductDetail.as_view(), name='product_detail'),
    path('new/', views.ProductNew.as_view(), name='product_new'),
    path('<int:product_id>/update/', views.ProductUpdate.as_view(), name='product_update'),
    ]
