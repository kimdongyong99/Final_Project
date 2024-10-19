# models.py
from django.db import models
from django.conf import settings

class Product(models.Model):
    name = models.CharField(max_length=100)  # 상품명
    price = models.DecimalField(max_digits=10, decimal_places=2)  # 가격
    description = models.TextField()  # 상품 설명
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)  # 상품 이미지
    created_at = models.DateTimeField(auto_now_add=True)  # 등록 시간

    def __str__(self):
        return self.name


class Payment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # 커스텀 사용자 모델 참조
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.user.username} - {self.product.name} 결제"
