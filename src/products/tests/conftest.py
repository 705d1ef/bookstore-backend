import pytest
from products.models import Book


@pytest.fixture
def book_fixture():
    return Book.objects.create(title="Test_book 1", price=25, author="Test_author 1")
