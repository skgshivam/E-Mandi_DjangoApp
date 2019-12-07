# Generated by Django 2.2.7 on 2019-12-04 16:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crop', '0002_watchlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watchlist',
            name='crop',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='crop.Crop'),
        ),
        migrations.AlterField(
            model_name='watchlist',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]