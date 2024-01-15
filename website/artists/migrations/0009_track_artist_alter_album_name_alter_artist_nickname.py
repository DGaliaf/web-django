# Generated by Django 4.2.3 on 2024-01-15 05:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0008_alter_subscribeform_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='track',
            name='artist',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='artists.artist'),
        ),
        migrations.AlterField(
            model_name='album',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='artist',
            name='nickname',
            field=models.CharField(max_length=255, unique=True, verbose_name='Псевдоним'),
        ),
    ]
