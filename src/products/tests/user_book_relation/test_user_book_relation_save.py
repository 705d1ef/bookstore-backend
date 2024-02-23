import pytest

from products.models import Book, UserBookRelation
from django.contrib.auth.models import User


@pytest.mark.django_db
def test_save_method(mocker):
    "test to check that set_rating function called only when it needed to reset rating"

    set_rating = mocker.patch("products.services.set_rating")

    user3 = User.objects.create(username="user3", first_name="1", last_name="2")
    book_111 = Book.objects.create(title="Test book 1", price=25, author="Author 1")
    user_book_3 = UserBookRelation.objects.create(
        user=user3, book=book_111, like=True, rate=4
    )
    user_book_3.rate = 4
    user_book_3.save()

    set_rating.assert_called_once()
