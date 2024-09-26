import random
from django.core.mail import send_mail
from django.conf import settings

# 인증번호 생성 함수
def generate_verification_code():
    return str(random.randint(100000, 999999))  # 6자리 숫자 인증번호 생성

# 이메일로 인증번호 전송하는 함수
def send_verification_email(user_email, verification_code):
    subject = 'Your Verification Code'
    message = f'Your verification code is: {verification_code}'
    email_from = settings.EMAIL_HOST_USER  # settings.py에서 설정한 발신자 이메일 사용
    send_mail(subject, message, email_from, [user_email])  # 이메일 발송