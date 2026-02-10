from unittest import TestCase

from flask_dummyimage import get_size


class SizeTest(TestCase):
    def test_get_size(self):
        self.assertEqual((200, 200), get_size("200"))
        self.assertEqual((640, 480), get_size("640x480"))
