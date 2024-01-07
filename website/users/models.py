from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=255, blank=False, verbose_name="Телефон")
    name = models.CharField(max_length=255, blank=False, verbose_name="Имя")
    lastName = models.CharField(max_length=255, blank=False, verbose_name="Фамилия")
    surname = models.CharField(max_length=255, blank=False, verbose_name="Отчество")
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
