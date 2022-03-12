from rest_framework.serializers import ModelSerializer
from rest_framework.exceptions import ValidationError
from .models import *


class ArtistSerial(ModelSerializer):
    class Meta:
        model = Artist
        fields = ['id', 'name', 'direction', 'description', 'image']

    def validate_name(self, value):
        if len(value) <= 3:
            raise ValidationError(detail="Such name of artist doesn't exist in database!")
        return value

class AlbumSerial(ModelSerializer):
    class Meta:
        model = Album
        fields = ['id', 'title', 'date', 'cover', 'artist']

    def validate_title(self, value):
        if len(value) <= 4:
            raise ValidationError(detail="Such title of album doesn't exist in database!")
        return value

class SongSerial(ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'title', 'cover', 'lyrics', 'duration', 'source', 'album']

    def validate_title(self, value):
        if len(value) <= 4:
            raise ValidationError(detail="Such title of album doesn't exist in database!")
        return value