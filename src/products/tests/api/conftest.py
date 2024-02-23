import pytest
from products.models import Book


@pytest.fixture
def user_fixture(client, django_user_model):
    user = django_user_model.objects.create(
        username="test_username", first_name="Keith", last_name="Howard"
    )
    client.force_login(user)
    return user


@pytest.fixture
def books_fixture():
    book_1 = Book.objects.create(title="Test book 1", price=25, author="Author 1")
    book_2 = Book.objects.create(title="Test book 2", price=55, author="Author 2")
    book_3 = Book.objects.create(title="Test book 3", price=75, author="Author 3")

    return book_1, book_2, book_3
