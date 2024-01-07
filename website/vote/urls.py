from django.urls import path

from . import views

app_name = 'vote'
urlpatterns = [
    path('', views.vote, name='vote_page'),
]