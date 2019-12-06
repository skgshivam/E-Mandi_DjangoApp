# Generated by Django 2.2.7 on 2019-11-22 18:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('order', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.FloatField(default=0.0)),
                ('review', models.CharField(default='', max_length=500)),
                ('revieweduser', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='revieweduser', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(default='', max_length=100)),
                ('phone', models.BigIntegerField(default=0)),
                ('image', models.ImageField(blank=True, upload_to='image_profile')),
                ('state', models.CharField(default='', max_length=100)),
                ('city', models.CharField(default='', max_length=100)),
                ('street', models.CharField(default='', max_length=500)),
                ('aadharcard', models.BigIntegerField(default=0)),
                ('pincode', models.IntegerField(default=0)),
                ('email_confirmed', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.FloatField(default=0.0)),
                ('review', models.CharField(default='', max_length=500)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.ExecutedOrder')),
            ],
        ),
    ]
