from django.contrib import admin
from django.urls import path, include
from music.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('artist', ArtistViewSet),
router.register('album', AlbumViewSet),
router.register('song', SongViewSet),


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
