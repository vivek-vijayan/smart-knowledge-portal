# Generated by Django 4.2.1 on 2023-07-06 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DatabaseEngine', '0003_employee_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='offboard_started',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='employee',
            name='onboard_started',
            field=models.BooleanField(default=False),
        ),
    ]
