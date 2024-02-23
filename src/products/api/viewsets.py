from django.db.models import Case, Count, When
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.mixins import UpdateModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from products.api.serializers import BooksSerializer, UserBookRelationSerializer
from products.models import Book, UserBookRelation


class BookViewSet(ModelViewSet):
    queryset = (
        Book.objects.all()
        .annotate(likes_count=Count(Case(When(userbookrelation__like=True, then=1))))
        .prefetch_related("customers")
        .order_by("id")
    )
    serializer_class = BooksSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["price"]
    search_fields = ["author", "title"]
    ordering_fields = ["price", "author", "publication_date"]


class UserBookRelationView(UpdateModelMixin, GenericViewSet):
    permission_classes = [IsAuthenticated]
    queryset = UserBookRelation.objects.all()
    serializer_class = UserBookRelationSerializer
    lookup_field = "book"

    def get_object(self):
        """
        Custom method to get or create relation between user and book
        """
        obj, _ = UserBookRelation.objects.get_or_create(
            user=self.request.user, book_id=self.kwargs["book"]
        )

        return obj
