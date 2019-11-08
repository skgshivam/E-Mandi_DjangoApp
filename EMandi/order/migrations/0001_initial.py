# Generated by Django 2.2.5 on 2019-11-08 18:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MarketOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CropName', models.CharField(max_length=50)),
                ('CropVariety', models.CharField(max_length=50)),
                ('Quantity', models.PositiveIntegerField(default=None)),
                ('OrderDate', models.DateTimeField(auto_now_add=True)),
                ('ClosingDate', models.DateField()),
                ('ProductionMode', models.CharField(max_length=50)),
                ('BasePrice', models.FloatField(default=None)),
                ('OrderStatus', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3')], max_length=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ExecutedOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now=True)),
                ('commision', models.FloatField(default=None)),
                ('buyerid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('orderid', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='order.MarketOrder')),
            ],
        ),
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(default=None)),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='order.MarketOrder')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
