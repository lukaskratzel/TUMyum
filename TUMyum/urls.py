from django.contrib import admin
from django.urls import path, include
from api import urls as api_urls
from .views import BaseView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_urls, namespace='api')),
    path('', BaseView.as_view(), name="home")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
