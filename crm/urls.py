from django.urls import path
from . import views
urlpatterns = [
    path('',views.Home,name="home"),
    path('customer/<str:pk>/',views.customer,name="customer"),
    path('products',views.products,name="products"),
    path('create_order/',views.createOrder,name="create_order"),
    path('update_order/<str:pk>',views.UpdateOrder,name="update_order"),
    path('delete_order/<str:pk>',views.DeleteOrder,name="delete_order"),
]
