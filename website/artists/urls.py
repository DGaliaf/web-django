from django.urls import path

from . import views

app_name = 'artists'
urlpatterns = [
    path('details/<int:pk>/<nickname>', views.ArtistDetailView.as_view(), name='artist_detail'),
]
