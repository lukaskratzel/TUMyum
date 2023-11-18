from django.urls import path
from .views import get_rating, post_rating

app_name = "api"

urlpatterns = (
    path('getRating/', get_rating, name='get_rating'),
    path('postRating/', post_rating, name='post_rating')
)