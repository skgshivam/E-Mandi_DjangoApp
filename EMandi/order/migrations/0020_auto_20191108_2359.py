# Generated by Django 2.2.6 on 2019-11-08 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0019_auto_20191108_2344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marketorder',
            name='OrderDate',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
