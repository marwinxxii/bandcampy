import unittest
from unittest.mock import patch

import bandcampy

ALBUM_FILE = 'album.html'
TRACK_FILE = 'track.html'

URL = 'http://topshelfrecords.bandcamp.com/album/lacuna'

class BandcampTestCase(unittest.TestCase):

    @patch('bandcampy.get_page')
    def test_get_album_data(self, open_stream_mock):
        with open(ALBUM_FILE) as f:
            open_stream_mock.return_value = f.read()
        actual = bandcampy.get_embed_data(URL)
        expected = {
            'artist': 'Caravels',
            'artist_id': 1596630884,
            'album_title': 'Lacuna',
            'album_id': 1335340116,
            'base_url': 'http://bandcamp.com'
        }
        self.assertEqual(actual, expected)

    @patch('bandcampy.get_page')
    def test_get_track_data(self, open_stream_mock):
        with open(TRACK_FILE) as f:
            open_stream_mock.return_value = f.read()
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
