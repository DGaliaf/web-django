# Generated by Django 4.2.3 on 2024-01-04 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0004_delete_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='image',
            field=models.ImageField(blank=True, default='default.jpg', max_length=255, upload_to='artist_pics', verbose_name='Изображение'),
        ),
    ]