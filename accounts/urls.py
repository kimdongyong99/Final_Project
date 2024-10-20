from django.urls import path, include
from . import views


urlpatterns = [
    path("signup/", views.SignupView.as_view()),
    path("login/", views.LoginView.as_view()),
    path("logout/", views.LogoutView.as_view()),
    path(
        "email-verification/",
        views.RequestEmailVerificationView.as_view(),
        name="request-email-verification",
    ),
    path("verify-email/", views.VerifyEmailView.as_view(), name="verify-email"),
    path("<str:username>/", views.UserProfileView.as_view()),
]
