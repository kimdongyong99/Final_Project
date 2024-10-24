from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/accounts/", include("accounts.urls")),
    path("api/posts/", include("posts.urls")),
    path("api/articles/", include("articles.urls")),
    path("api/chat_gpt/", include("chatgpt.urls")),
    path("api/payment/", include("payment.urls")),
    path("", TemplateView.as_view(template_name="index.html")),
]


# 미디어 파일 제공 설정 추가
if settings.DEBUG:  # DEBUG 모드일 때만 미디어 파일을 제공
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
