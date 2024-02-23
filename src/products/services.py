from django.db.models import Avg

from products.models import UserBookRelation


def set_rating(book):  # type: ignore
    rating = (
        UserBookRelation.objects.filter(book=book)
        .aggregate(rating=Avg("rate"))
        .get("rating")
    )
    book.rating = rating
    book.save()
