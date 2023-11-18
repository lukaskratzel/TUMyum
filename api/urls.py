from django.urls import path
from .views import get_rating, post_rating

app_name = "api"

urlpatterns = (
    path('get_rating/', get_rating, name='get_rating'),
    path('post_rating/', post_rating, name='post_rating')
)