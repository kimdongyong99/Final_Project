from django.urls import path
from .views import PaymentList

urlpatterns = [
    path('purchase/', PaymentList.as_view()),
]