from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from artists.views import index

urlpatterns = [
    path("", index, name="index"),
    path("artists/", include("artists.urls")),
    path("user/", include("users.urls")),
    path("", include('polls.urls')),
    path("admin/", admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
