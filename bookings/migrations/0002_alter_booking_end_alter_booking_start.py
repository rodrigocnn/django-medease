# Generated by Django 4.1.3 on 2023-06-25 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='end',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='booking',
            name='start',
            field=models.IntegerField(),
        ),
    ]