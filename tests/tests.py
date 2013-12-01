import unittest
from unittest.mock import patch

import bandcampy

ALBUM_FILE = 'album.html'
TRACK_FILE = 'track.html'

URL = 'http://topshelfrecords.bandcamp.com/album/lacuna'

class BandcampTestCase(unittest.TestCase):

    @patch('bandcampy.open_stream')
    def test_get_album_data(self, open_stream_mock):
        open_stream_mock.return_value = open(ALBUM_FILE)
        actual = bandcampy.get_embed_data(URL)
        expected = {
            'artist': 'Caravels',
            'artist_id': 1596630884,
            'album_title': 'Lacuna',
            'album_id': 1335340116,
            'base_url': 'http://bandcamp.com'
        }
        self.assertEqual(actual, expected)

    @patch('bandcampy.open_stream')
    def test_get_track_data(self, open_stream_mock):
        open_stream_mock.return_value = open(TRACK_FILE)
        actual = bandcampy.get_embed_data(URL)
        expected = {
            'artist': 'Caravels',
            'artist_id': 1596630884,
            'album_title': 'Lacuna',
            'album_id': 1335340116,
            'base_url': 'http://bandcamp.com',
            'track': 6
        }
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
