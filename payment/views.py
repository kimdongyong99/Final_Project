from django.shortcuts import render

# Create your views here.
from django.conf import settings
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from .models import Payment
from .serializers import PaymentSerializer
import time
import requests


class PaymentList(generics.ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class PaymentAPIView(APIView):
    def post(self, request):
        amount = request.data.get('amount')
        user = request.user

        # 아임포트 API 요청을 위한 인증 토큰 발급
        auth_response = requests.post(
            'https://api.iamport.kr/users/getToken',
            data={
                'imp_key': settings.IAMPORT['IMP_KEY'],
                'imp_secret': settings.IAMPORT['IMP_SECRET'],
            }
        )

        if auth_response.status_code != 200:
            return Response({'message': '아임포트 인증 실패'}, status=400)

        access_token = auth_response.json()['response']['access_token']

        # 결제 요청
        headers = {'Authorization': access_token}
        payment_data = {
            'merchant_uid': 'order_' + str(user.id) + str(time.time()),
            'name': '결제',
            'amount': amount,
            'buyer_name': user.username,
            'buyer_email': user.email,
            'buyer_tel': user.profile.phone_number,
        }

        response = requests.post(
            'https://api.iamport.kr/payments/onetime',
            headers=headers,
            data=payment_data
        )

        if response.status_code == 200 and response.json()['response']['status'] == 'paid':
            imp_uid = response.json()['response']['imp_uid']
            Payment.objects.create(user=user, amount=amount, imp_uid=imp_uid)
            return Response({'message': '결제 성공'}, status=200)
        else:
            fail_reason = response.json().get('message', '결제 실패')
            return Response({'message': '결제 실패', 'error': fail_reason}, status=400)