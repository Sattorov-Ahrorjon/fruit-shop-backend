from django.urls import path
from .views import UserViewSet, ProductViewSet, OrderViewSet

urlpatterns = [
    path('user/', UserViewSet.as_view({'post': 'user_create', 'get': 'user_list'})),
    path('user/<int:pk>/', UserViewSet.as_view({'get': 'user_detail'})),
    path('product/', ProductViewSet.as_view({'get': 'product_list'})),
    path('product/<int:pk>/', ProductViewSet.as_view({'get': 'product_detail'})),
    path('order/', OrderViewSet.as_view({'post': 'order_create'})),
    path('order/<int:pk>/', OrderViewSet.as_view({'get': 'order_list'})),
    path('order/detail/<int:pk>/', OrderViewSet.as_view({'get': 'order_detail'})),
]
