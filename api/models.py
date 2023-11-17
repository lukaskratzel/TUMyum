from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import Avg


review_validators = [
    MinValueValidator(1),
    MaxValueValidator(5)
]

# Create your models here.
class Review(models.Model):
    name = models.CharField(max_length=200)
    stars = models.IntegerField(validators=review_validators)
    timestamp = models.DateTimeField(auto_now_add=True)

def get_average_stars_for(name):
    return Review.objects.filter(name=name).aggregate(average_rating=Avg('stars'))
