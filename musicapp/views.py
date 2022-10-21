from rest_framework import viewsets

from musicapp.serializers import ArtistSerilizer

from .models import *
from .serializers import *


class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class  = ArtistSerilizer


class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class  = SongSerilizer

    
class LyricViewSet(viewsets.ModelViewSet):
    queryset = Lyric.objects.all()
    serializer_class  = LyricSerilizer