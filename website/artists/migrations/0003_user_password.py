# Generated by Django 4.2.3 on 2023-12-13 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0002_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default='0', max_length=255, verbose_name='Пароль'),
        ),
    ]