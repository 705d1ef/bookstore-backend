from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from products.models import Book, UserBookRelation


class BookCustomerSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name", "last_name"]


class BooksSerializer(ModelSerializer):
    likes_count = serializers.IntegerField(read_only=True)
    rating = serializers.DecimalField(
        max_digits=3, decimal_places=2, read_only=True, coerce_to_string=False
    )
    customers = BookCustomerSerializer(many=True, read_only=True)
    price = serializers.DecimalField(
        max_digits=7, decimal_places=2, coerce_to_string=False
    )

    class Meta:
        model = Book

        # fields = ["rating"]
        fields = (
            "id",
            "title",
            "cover",
            "author",
            "likes_count",
            "price",
            "rating",
            "customers",
            "description",
            "number_of_pages",
        )
        # read_only_fields = [
        #    "id",
        #    "author",
        #    "cover",
        #    "description",
        #    "dimensions",
        #    "genre",
        #    "language",
        #    "title",
        #    "number_of_pages",
        #    "price",
        #    "publication_date",
        #    "likes_count",
        #    "rating",
        #    "customers",
        # ]

        # fields = ("__all__")


class UserBookRelationSerializer(ModelSerializer):
    class Meta:
        model = UserBookRelation
        # exclude = ["user"]
        fields = "__all__"
        # fields = ["book", "like", "add_to_list", "rate"]
