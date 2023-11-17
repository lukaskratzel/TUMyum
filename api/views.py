from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import get_average_stars_for, Review



# Create your views here.

@api_view(['GET'])
def get_rating(request):
    name = request.query_params.get('name', None)
    ## -- input validation --
    if not name or type(name) != str:
        return Response({'error': 'please provide a valid name'}, status=status.HTTP_400_BAD_REQUEST)
    ## -- end input validation --
    avg_rating = get_average_stars_for(name)
    return Response({'rating': avg_rating}, status=status.HTTP_200_OK)
    
@api_view(['POST'])
def post_rating(request):
    name = request.data.get('name', None)
    rating = request.data.get('rating', None)
    ## -- input validation --
    if not name or type(name) != str:
        return Response({'error': 'please provide a valid name'}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        if not rating:
            raise Exception
        rating = int(rating)
        if not 1 <= rating <= 5:
            raise Exception
    except:
        return Response({'error': 'please provide a valid rating'}, status=status.HTTP_400_BAD_REQUEST)
    ## -- end input validation --
    Review.objects.create(name=name, rating=rating)
    return Response({'message', 'Review created successfully'}, status=status.HTTP_200_OK)