from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from artists.views import index
from users import views as user_views

urlpatterns = [
    path("", index, name="index"),
    path("artists/", include(("artists.urls", "artists"), namespace="artists")),
    path("user/", include(("users.urls", "users"), namespace="users")),
    path("vote/", include(("vote.urls", "users"), namespace="vote")),
    # path('register/', user_views.register, name='register'),
    path("admin/", admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
