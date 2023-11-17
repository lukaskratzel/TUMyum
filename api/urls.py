from django.urls import path
from .views import get_rating, post_rating

urlpatterns = (
    path('get_rating/', get_rating, name='get_rating'),
    path('post_rating/', post_rating, name='post_rating')
)