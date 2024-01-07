from django.conf import settings
from django.db import models


class SubscribeForm(models.Model):
    email = models.EmailField(blank=False, unique=True)
    phone = models.CharField(max_length=255, unique=True, blank=False, verbose_name="Телефон")
    receive_adv = models.BooleanField(verbose_name="Получать рекламу")


class Artist(models.Model):
    image = models.ImageField(max_length=255, blank=True, verbose_name="Изображение", default="default.jpg", upload_to='artist_pics')
    nickname = models.CharField(max_length=255, blank=False, verbose_name="Псевдоним")
    name = models.CharField(max_length=255, blank=True, verbose_name="Имя")
    surname = models.CharField(max_length=255, blank=True, verbose_name="Фамилия")
    age = models.PositiveIntegerField(default=0, verbose_name="Возраст")
    shortBio = models.TextField(blank=True, verbose_name="Короткое БИО")
    bio = models.TextField(blank=True, verbose_name="БИО")

    def __str__(self):
        return self.nickname

class Album(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=False)
    description = models.TextField(blank=True)
    release_date = models.DateField()

    def __str__(self):
        return self.name

class Track(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=255, blank=False)
    duration = models.DurationField()
    description = models.TextField(max_length=255, blank=True)
    release_date = models.DateField()

    def __str__(self):
        return self.name
