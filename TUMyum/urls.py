from django.contrib import admin
from django.urls import path, include
from api import urls as api_urls
from .views import BaseView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_urls, namespace='api')),
    path('', BaseView.as_view(), name="home")
]
