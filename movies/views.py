from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MovieSerializer
from .models import MovieData


class MovieViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.all()
    serializer_class = MovieSerializer


class DefaultViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.filter(category='N/A')
    serializer_class = MovieSerializer