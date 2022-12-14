import pytest


@pytest.mark.django_db
def test_ad_create(client, user, category):
    response = client.post('/ad/create/', {
            'name': 'pytesttestt',
            'author': user.pk,
            'price': 10,
            'description': None,
            'is_published': False,
            'image': None,
            'category': category.pk
        }, content_type='application/json')
    assert response.status_code == 201
    assert response.data == {
            'id': 1,
            'name': 'pytesttestt',
            'author': user.pk,
            'price': 10,
            'description': None,
            'is_published': False,
            'image': None,
            'category': category.pk
        }
