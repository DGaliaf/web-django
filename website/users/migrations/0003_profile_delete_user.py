# Generated by Django 4.2.3 on 2024-01-04 08:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0002_user_lastname_user_name_user_surname'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=255, verbose_name='Телефон')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('lastName', models.CharField(max_length=255, verbose_name='Фамилия')),
                ('surname', models.CharField(max_length=255, verbose_name='Отчество')),
                ('image', models.ImageField(default='default.jpg', upload_to='profile_pics')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]