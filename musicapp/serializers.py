from rest_framework import serializers

from .models import *


class ArtistSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'


class SongSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'


class LyricSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Lyric
        fields = '__all__'