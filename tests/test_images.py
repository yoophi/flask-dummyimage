from io import BytesIO

import pytest
from flask import Flask
from PIL import Image

from flask_dummyimage import DummyImage, get_size


@pytest.fixture
def client():
    app = Flask(__name__)
    app.config['TESTING'] = True
    DummyImage(app)
    return app.test_client()


@pytest.mark.parametrize('size,expected', [
    ('200', (200, 200)),
    ('640x480', (640, 480)),
])
def test_size(size, expected):
    assert get_size(size) == expected


@pytest.mark.parametrize('path,expected', [
    ('', (320, 320)),
    ('/64', (64, 64)),
    ('/80x40', (80, 40)),
])
def test_png_response(client, path, expected):
    response = client.get('/dummyimage/dummyimage' + path)
    assert response.status_code == 200
    assert response.mimetype == 'image/png'
    with Image.open(BytesIO(response.data)) as image:
        image.load()
        assert image.size == expected
        assert image.mode == 'RGB'


def test_custom_rendering(client):
    response = client.get('/dummyimage/dummyimage/80x40', query_string={
        'text': 'Safe', 'zoom': 'false', 'fontsize': '12',
        'bg_color': '!123', 'border_color': 'red', 'debug': 'true',
    })
    assert response.status_code == 200
    with Image.open(BytesIO(response.data)) as image:
        assert image.getpixel((0, 0)) == (255, 0, 0)
        assert image.getpixel((1, 1)) == (17, 34, 51)


def test_border_can_be_disabled(client):
    response = client.get('/dummyimage/dummyimage/64', query_string={
        'border': 'false', 'bg_color': 'blue', 'text': 'OK',
    })
    assert response.status_code == 200
    with Image.open(BytesIO(response.data)) as image:
        assert image.getpixel((0, 0)) == (0, 0, 255)
