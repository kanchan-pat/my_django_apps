#-----------------------Imports-------------------------------
from django.urls import path
from product_app import views

#-----------------------Url Patterns-------------------------------

urlpatterns = [
    path('', views.ProductList.as_view(), name='product_list'),
    path('product/<int:pk>/', views.ProductDetail.as_view(), name='product_detail'),
    path('new/', views.ProductNew.as_view(), name='product_new'),
    path('<int:pk>/update/', views.ProductUpdate.as_view(), name='product_update'),
    path('<int:pk>/delete/', views.ProductDelete.as_view(), name='product_delete')
]
