from django.shortcuts import render
from rest_framework.filters import OrderingFilter , SearchFilter
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import *
from .serializers import *


# Create your views here.

class ArtistViewSet(ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerial
    filter_backends = [SearchFilter]
    search_fields = ['name','direction',]
    @action(detail=True, methods=['GET'])
    def album(self, request, *args, **kwargs):
        artist = self.get_object()
        al = Album.objects.filter(artist=artist)
        serializer = AlbumSerial(al, many=True)
        return Response(serializer.data)

class AlbumViewSet(ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerial
    filter_backends = [OrderingFilter]
    oredering_fields = ['date',]
    @action(detail=True, methods=['GET'])
    def album(self, request, *args, **kwargs):
        song = self.get_object()
        sg = Song.objects.filter(song=song)
        serializer = SongSerial(sg, many=True)
        return Response(serializer.data)

class SongViewSet(ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerial
    filter_backends = [OrderingFilter]
    oredering_fields = ['duration',]
    def song(self, request, *args, **kwargs):
        song = self.get_object()
        sg = Song.objects.filter(song=song)
        serializer = SongSerial(sg, many=True)
        return Response(serializer.data)
