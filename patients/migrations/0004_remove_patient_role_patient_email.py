# Generated by Django 4.1.3 on 2023-06-13 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0003_patient_role'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='role',
        ),
        migrations.AddField(
            model_name='patient',
            name='email',
            field=models.CharField(max_length=80, null=True, unique=True),
        ),
    ]
