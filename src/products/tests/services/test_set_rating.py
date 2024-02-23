import pytest
from products.services import set_rating
from decimal import Decimal
from products.models import UserBookRelation


@pytest.mark.django_db
def test_average_rating(django_user_model, book_fixture):
    user1 = django_user_model.objects.create(
        username="user1", first_name="Thomas", last_name="Knox"
    )
    user2 = django_user_model.objects.create(
        username="user2", first_name="Theresa", last_name="Blake"
    )
    user3 = django_user_model.objects.create(
        username="user3", first_name="Lucas", last_name="Gibson"
    )
    UserBookRelation.objects.create(user=user1, book=book_fixture, like=True, rate=5)
    UserBookRelation.objects.create(user=user2, book=book_fixture, like=True, rate=5)
    UserBookRelation.objects.create(user=user3, book=book_fixture, like=True, rate=4)

    set_rating(book_fixture)
    book_fixture.refresh_from_db()

    assert book_fixture.rating == Decimal("4.67")
