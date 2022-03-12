from unittest import TestCase
from music.models import Artist, Album, Song
from music.serializers import ArtistSerial

class TestArtistSerial(TestCase):
    def setUp(self) -> None:
        self.artist1 = Artist.objects.create(
            name='Ozodbek Nazarberkov',
            direction='Classic',
            description='Ozbekiston xalq astisti'
        )
    def test_artist(self):
        a = Artist.objects.all()
        malumot = ArtistSerial(a, many=True)
        assert malumot.data[0]['id'] == 1
        self.assertTrue(malumot.data[0]['id'] == 1)
        self.assertEqual(malumot.data[0]['id'], 1)
        assert malumot.data[0]['name'] == 'Ozodbek Nazarberkov'
        assert malumot.data[0]['image'] == ''
        assert malumot.data[1]['name'] == 'Adele'
        assert malumot.data[1]['image'] == ''
        assert malumot.data[1]['description'] == ''

