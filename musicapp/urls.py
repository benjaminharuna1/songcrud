from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register(r'artist', ArtistViewSet, basename='artist')
router.register(r'song', SongViewSet, basename='song')
router.register(r'lyric', LyricViewSet, basename='lyric')

urlpatterns = [] + router.urls

# 127.0.0.1:8000/artist
