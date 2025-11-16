from django.shortcuts import render, get_object_or_404
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Joke, Picture
from .serializers import JokeSerializer, PictureSerializer
import random


# HTML Views
def random_view(request):
    """Display a random joke and random picture"""
    jokes = Joke.objects.all()
    pictures = Picture.objects.all()

    joke = random.choice(jokes) if jokes else None
    picture = random.choice(pictures) if pictures else None

    return render(request, 'dadjokes/random.html', {
        'joke': joke,
        'picture': picture
    })


def jokes_view(request):
    """Display all jokes"""
    jokes = Joke.objects.all()
    return render(request, 'dadjokes/jokes.html', {'jokes': jokes})


def joke_detail_view(request, pk):
    """Display a single joke by ID"""
    joke = get_object_or_404(Joke, pk=pk)
    return render(request, 'dadjokes/joke_detail.html', {'joke': joke})


def pictures_view(request):
    """Display all pictures"""
    pictures = Picture.objects.all()
    return render(request, 'dadjokes/pictures.html', {'pictures': pictures})


def picture_detail_view(request, pk):
    """Display a single picture by ID"""
    picture = get_object_or_404(Picture, pk=pk)
    return render(request, 'dadjokes/picture_detail.html', {'picture': picture})


# REST API Views
@api_view(['GET'])
def api_random_joke(request):
    """Get a random joke"""
    jokes = Joke.objects.all()
    if jokes:
        joke = random.choice(jokes)
        serializer = JokeSerializer(joke)
        return Response(serializer.data)
    return Response({'error': 'No jokes available'}, status=status.HTTP_404_NOT_FOUND)


class JokeListCreateAPIView(generics.ListCreateAPIView):
    """List all jokes (GET) or create a new joke (POST)"""
    queryset = Joke.objects.all()
    serializer_class = JokeSerializer


class JokeDetailAPIView(generics.RetrieveAPIView):
    """Retrieve a single joke by ID (GET)"""
    queryset = Joke.objects.all()
    serializer_class = JokeSerializer


class PictureListAPIView(generics.ListAPIView):
    """List all pictures (GET)"""
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer


class PictureDetailAPIView(generics.RetrieveAPIView):
    """Retrieve a single picture by ID (GET)"""
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer


@api_view(['GET'])
def api_random_picture(request):
    """Get a random picture"""
    pictures = Picture.objects.all()
    if pictures:
        picture = random.choice(pictures)
        serializer = PictureSerializer(picture)
        return Response(serializer.data)
    return Response({'error': 'No pictures available'}, status=status.HTTP_404_NOT_FOUND)
