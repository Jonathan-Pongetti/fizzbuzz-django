from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import FizzBuzz
from .serializers import FizzBuzzSerializer

# Create your views here.
@api_view(['GET'])
def getRoutes(request):
    """
    Get available API routes.
    """
    routes = [
        {
        "Endpoint":"/fizzbuzz",
        "method": "GET",
        "body": None,
        "description": "Returns list of all fizzbuzz objects"
        },
        {
        "Endpoint":"/fizzbuzz/id",
        "method": "GET",
        "body": None,
        "description": "Returns a single fizzbuzz object"
        },
        {
        "Endpoint":"/fizzbuzz",
        "method": "POST",
        "body": None,
        "description": "Creates a new fizzbuzz object"
        },
        ]
    return Response(routes)

@api_view(["GET", "POST"])
def fizzBuzz(request):
    """
    get:
    Return a list of all the existing fizzbuzzes.

    post:
    Create a new fizzbuzz instance.
    """
    if request.method == 'GET':
        fizzbuzz_list = FizzBuzz.objects.all()
        serializer = FizzBuzzSerializer(fizzbuzz_list, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = request.data
        fizzbuzz = FizzBuzz.objects.create(
            user_agent=request.META.get('HTTP_USER_AGENT', ''),
            message=data['message'] if 'message' in data else None
        )

        serializer = FizzBuzzSerializer(fizzbuzz, many=False)
        return Response(serializer.data)

@api_view(["GET"])
def getFizzBuzz(request, pk):
    """
    Get an individual fizzbuzz.
    """
    fizzbuzz = FizzBuzz.objects.get(id=pk)
    serializer = FizzBuzzSerializer(fizzbuzz, many=False)
    return Response(serializer.data)