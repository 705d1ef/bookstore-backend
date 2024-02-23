import debug_toolbar
from django.conf.urls import include
from django.contrib import admin
from django.urls import path

from products.api.router import product_router

urlpatterns = [
    path("admin/", admin.site.urls),
    path("__debug__/", include(debug_toolbar.urls)),
    path("", include(product_router.urls)),
]

