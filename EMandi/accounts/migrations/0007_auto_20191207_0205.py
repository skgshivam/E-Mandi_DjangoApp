# Generated by Django 2.2.7 on 2019-12-06 20:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20191204_1918'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='email_confirmed',
        ),
        migrations.DeleteModel(
            name='OrderReview',
        ),
    ]
