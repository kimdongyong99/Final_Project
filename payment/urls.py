from django.urls import path
from .views import ProductListView, ProductDetailView, PaymentCompleteView

urlpatterns = [
    path('products/', ProductListView.as_view(), name='product-list'),  # 상품 목록
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),  # 상품 디테일
    path('complete/', PaymentCompleteView.as_view(), name='payment-complete'),
]
