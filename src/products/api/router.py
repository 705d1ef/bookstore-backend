from rest_framework.routers import SimpleRouter

from products.api.viewsets import BookViewSet, UserBookRelationView

# from django.urls import include

product_router = SimpleRouter()

product_router.register(r"book", BookViewSet)
product_router.register(r"book_relation", UserBookRelationView)
