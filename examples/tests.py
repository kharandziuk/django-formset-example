import pytest
from examples import models

pytestmark = pytest.mark.django_db

def test_smoke(django_app):
    response = django_app.get('/')
    form = response.form
    form['name'] = 'owner'
    form['aggregate_set-0-name'] = 'owner'
    response.showbrowser()
    form.submit()
    assert models.Owner.objects.count() == 1
    assert models.Aggregate.objects.count() == 1
