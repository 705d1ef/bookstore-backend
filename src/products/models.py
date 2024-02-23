# from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=255, verbose_name="Title")
    author = models.CharField(max_length=255, verbose_name="Author")
    cover = models.ImageField(
        verbose_name="Cover", blank=True, help_text="The image of book", upload_to="assets/products"
    )
    description = models.TextField(verbose_name="Description", blank=True)
    dimensions = models.CharField(max_length=255, verbose_name="Dimensions", blank=True)
    quantity = models.PositiveSmallIntegerField(verbose_name="In stock")
    genre = models.CharField(max_length=255, verbose_name="Genre", blank=True)
    number_of_pages = models.CharField(verbose_name="Number of pages", blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="Price")
    publication_date = models.CharField(verbose_name="Publication date", blank=True)
    customers = models.ManyToManyField(
        User, through="UserBookRelation", related_name="books"
    )
    rating = models.DecimalField(
        max_digits=3, decimal_places=2, default=None, null=True
    )

    def __str__(self) -> str:
        return f" Id {self.id}: {self.title}"  # type: ignore


class UserBookRelation(models.Model):
    def __init__(self, *args, **kwargs):  # type: ignore
        super().__init__(*args, **kwargs)
        self.old_rate = self.rate

    RATE_CHOICES = (
        (1, "Poor"),
        (2, "Below average"),
        (3, "Average"),
        (4, "Above average"),
        (5, "Excellent"),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    like = models.BooleanField(default=False, blank=True)
    add_to_list = models.BooleanField(verbose_name="Add to List", default=False)
    rate = models.PositiveSmallIntegerField(choices=RATE_CHOICES, null=True, default=False, blank=True)

    def __str__(self) -> str:
        return (
            f" {self.user.username}: {self.book.title}, RATE {self.rate}"  # type ignore
        )

    def save(self, *args, **kwargs):  # type: ignore
        creating = not self.pk

        super().save(*args, **kwargs)

        if self.old_rate != self.rate or creating and self.old_rate is not None:
            from products.services import set_rating

            set_rating(self.book)

