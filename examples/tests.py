import pytest

pytestmark = pytest.mark.django_db

def test_smoke(django_app):
    response = django_app.get('/')
    assert response.text == 'Hello world!\n'
