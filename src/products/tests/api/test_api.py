import pytest
import json
from products.api.serializers import BooksSerializer
from products.models import Book, UserBookRelation
from django.db import connection
from django.db.models import Case, Count, When
from django.test.utils import CaptureQueriesContext
from django.urls import reverse


pytestmark = [pytest.mark.django_db]


@pytest.fixture
def url_books_list_fixture():
    url = reverse("book-list")

    return url


def test_get(client, books_fixture, url_books_list_fixture, django_user_model):
    user1 = django_user_model.objects.create(
        username="user1", first_name="Keith", last_name="Howard"
    )
    UserBookRelation.objects.create(
        user=user1, book=books_fixture[0], like=True, rate=5
    )
    with CaptureQueriesContext(connection) as queries:
        response = client.get(url_books_list_fixture)

    assert len(queries) == 2

    books = (
        Book.objects.all()
        .annotate(likes_count=Count(Case(When(userbookrelation__like=True, then=1))))
        .order_by("id")
    )
    data = BooksSerializer(books, many=True).data

    assert response.status_code == 200
    assert response.data == data
    assert data[0]["rating"] == "5.00"
    assert data[0]["likes_count"] == 1


def test_get_filter(client, books_fixture, url_books_list_fixture):
    books = (
        Book.objects.filter(id__in=[books_fixture[1].id, books_fixture[2].id])
        .annotate(likes_count=Count(Case(When(userbookrelation__like=True, then=1))))
        .order_by("id")
    )
    response = client.get(url_books_list_fixture, data={"price": 55})
    serializer_data = BooksSerializer(books, many=True).data

    assert response.status_code == 200
    assert [serializer_data[0]] == response.data


def test_get_search(client, books_fixture, url_books_list_fixture):
    books = (
        Book.objects.filter(id__in=[books_fixture[0].id, books_fixture[2].id])
        .annotate(likes_count=Count(Case(When(userbookrelation__like=True, then=1))))
        .order_by("id")
    )
    response = client.get(url_books_list_fixture, data={"search": "Author 1"})
    serializer_data = BooksSerializer(books, many=True).data

    assert response.status_code == 200
    assert [serializer_data[0]] == response.data


def test_create(client, url_books_list_fixture, books_fixture, django_user_model):
    assert Book.objects.all().count() == 3
    # print('count---->', Book.objects.all().count())
    user1 = django_user_model.objects.create(
        username="user1", first_name="Keith", last_name="Howard"
    )
    data = {
        "title": "Programming in Python 3",
        "price": 150,
        "author": "Mark Summerfield",
    }
    json_data = json.dumps(data)
    client.force_login(user1)
    response = client.post(
        url_books_list_fixture, data=json_data, content_type="application/json"
    )

    assert response.status_code == 201
    assert Book.objects.all().count() == 4


def test_update(client, books_fixture, django_user_model):
    user1 = django_user_model.objects.create(
        username="user1", first_name="Keith", last_name="Howard"
    )
    url = reverse("book-detail", args=(books_fixture[0].id,))
    data = {
        "title": books_fixture[0].title,
        "price": 575,
        "author": books_fixture[0].author,
    }
    json_data = json.dumps(data)
    client.force_login(user1)
    response = client.put(url, data=json_data, content_type="application/json")
    assert response.status_code == 200
    books_fixture[0].refresh_from_db()
    assert books_fixture[0].price == 575
