# views.py
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Product, Payment
from .serializers import ProductSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = None

# views.py
class ProductDetailView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class PaymentCompleteView(APIView):
    permission_classes = [IsAuthenticated]  # 로그인한 유저만 결제 가능

    def post(self, request):
        product_id = request.data.get('product_id')
        product = Product.objects.get(id=product_id)
        user = request.user  # 로그인된 유저 정보

        # 결제 정보 저장
        payment = Payment.objects.create(
            user=user,
            product=product,
            amount=product.price,  # 결제 금액
            status='paid',  # 결제 상태 (성공)
        )

        return Response({"message": "결제 정보가 성공적으로 저장되었습니다.", "payment_id": payment.id}, status=201)