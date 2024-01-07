# Generated by Django 4.2.3 on 2024-01-03 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='lastName',
            field=models.CharField(default=2, max_length=255, verbose_name='Фамилия'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(default=2, max_length=255, verbose_name='Имя'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='surname',
            field=models.CharField(default=2, max_length=255, verbose_name='Отчество'),
            preserve_default=False,
        ),
    ]