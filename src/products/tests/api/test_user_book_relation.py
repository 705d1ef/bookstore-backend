import pytest
import json
from products.models import UserBookRelation
from django.urls import reverse


pytestmark = [pytest.mark.django_db]


def test_likes(client, book_fixture, user_fixture):
    url = reverse("userbookrelation-detail", args=(book_fixture.id,))
    data = {"like": True}
    json_data = json.dumps(data)
    response = client.patch(url, data=json_data, content_type="application/json")

    assert response.status_code == 200
    relation = UserBookRelation.objects.get(user=user_fixture, book=book_fixture)
    assert relation.like is True


def test_add_to_list(client, user_fixture, book_fixture):
    url = reverse("userbookrelation-detail", args=(book_fixture.id,))
    data = {"add_to_list": True}
    json_data = json.dumps(data)
    response = client.patch(url, data=json_data, content_type="application/json")

    assert response.status_code == 200
    relation = UserBookRelation.objects.get(user=user_fixture, book=book_fixture)
    assert relation.add_to_list is True


def test_rate(client, user_fixture, book_fixture):
    url = reverse("userbookrelation-detail", args=(book_fixture.id,))
    data = {"rate": 3}
    json_data = json.dumps(data)
    response = client.patch(url, data=json_data, content_type="application/json")

    assert response.status_code == 200
    relation = UserBookRelation.objects.get(user=user_fixture, book=book_fixture)
    assert relation.rate == 3


def test_rate_wrong(client, book_fixture, user_fixture):
    """test must fail if rate is wrong"""

    url = reverse("userbookrelation-detail", args=(book_fixture.id,))
    data = {"rate": 9}
    json_data = json.dumps(data)
    client.force_login(user_fixture)
    response = client.patch(url, data=json_data, content_type="application/json")

    assert response.status_code == 400
