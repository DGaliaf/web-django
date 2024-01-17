from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from phonenumber_field.modelfields import PhoneNumberField


class City(models.Model):
    name = models.CharField(max_length=255, blank=False, verbose_name="Имя")
    zipcode = models.CharField(max_length=255, blank=False, verbose_name="ЗИП КОД")
    peopleNumbers = models.IntegerField(verbose_name="Населенность")

    def __str__(self):
        return f'{self.name}'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = PhoneNumberField(blank=False, verbose_name="Телефон", region="RU")
    name = models.CharField(max_length=255, blank=False, verbose_name="Имя")
    lastName = models.CharField(max_length=255, blank=False, verbose_name="Фамилия")
    surname = models.CharField(max_length=255, blank=False, verbose_name="Отчество")
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    city = models.ManyToManyField(City, verbose_name="Город проживания")

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
