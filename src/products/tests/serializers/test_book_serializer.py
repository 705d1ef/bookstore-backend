import pytest
from django.contrib.auth.models import User
from django.db.models import Case, Count, When
from collections import OrderedDict
from decimal import Decimal
from products.models import Book, UserBookRelation
from products.api.serializers import BooksSerializer


@pytest.mark.django_db
def test_serializer_data_is_ok():
    user11 = User.objects.create(
        username="user1", first_name="Keith", last_name="Howard"
    )
    user2 = User.objects.create(
        username="user2", first_name="Trevor", last_name="Scott"
    )
    user3 = User.objects.create(
        username="user3", first_name="Elizabeth", last_name="Rampling"
    )

    book_11 = Book.objects.create(title="Test book 1", price=25, author="Author 1")
    book_2 = Book.objects.create(title="Test book 2", price=55, author="Author 2")

    UserBookRelation.objects.create(user=user11, book=book_11, like=True, rate=5)
    UserBookRelation.objects.create(user=user2, book=book_11, like=True, rate=5)

    user_book_3 = UserBookRelation.objects.create(user=user3, book=book_11, like=True)

    user_book_3.rate = 4
    user_book_3.save()

    UserBookRelation.objects.create(user=user11, book=book_2, like=True, rate=3)
    UserBookRelation.objects.create(user=user2, book=book_2, like=True, rate=4)
    UserBookRelation.objects.create(user=user3, book=book_2, like=False)

    books = (
        Book.objects.all()
        .annotate(likes_count=Count(Case(When(userbookrelation__like=True, then=1))))
        .order_by("id")
    )

    data = BooksSerializer(books, many=True).data

    expected_data = [
        OrderedDict(
            [
                ("id", 21),
                ("title", "Test book 1"),
                ("cover", None),
                ("author", "Author 1"),
                ("likes_count", 3),
                ("price", Decimal("25.00")),
                ("rating", Decimal("4.67")),
                (
                    "customers",
                    [
                        OrderedDict([("first_name", "Keith"), ("last_name", "Howard")]),
                        OrderedDict([("first_name", "Trevor"), ("last_name", "Scott")]),
                        OrderedDict(
                            [("first_name", "Elizabeth"), ("last_name", "Rampling")]
                        ),
                    ],
                ),
                ("description", ""),
                ("number_of_pages", ""),
            ]
        ),
        OrderedDict(
            [
                ("id", 22),
                ("title", "Test book 2"),
                ("cover", None),
                ("author", "Author 2"),
                ("likes_count", 2),
                ("price", Decimal("55.00")),
                ("rating", Decimal("2.33")),
                (
                    "customers",
                    [
                        OrderedDict([("first_name", "Keith"), ("last_name", "Howard")]),
                        OrderedDict([("first_name", "Trevor"), ("last_name", "Scott")]),
                        OrderedDict(
                            [("first_name", "Elizabeth"), ("last_name", "Rampling")]
                        ),
                    ],
                ),
                ("description", ""),
                ("number_of_pages", ""),
            ]
        ),
    ]

    assert data == expected_data
