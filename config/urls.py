from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    # path("admin/", admin.site.urls),  # Removed the admin route
    path("api/", include("apps.core.urls")),
]
