from django.contrib import admin
from django.urls import path, include

app_name = "cinema"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/cinema/", include("cinema.urls", namespace="cinema")),
    path("__debug__/", include("debug_toolbar.urls")),
]
