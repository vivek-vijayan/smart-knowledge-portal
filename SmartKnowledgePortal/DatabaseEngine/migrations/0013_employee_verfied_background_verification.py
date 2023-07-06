# Generated by Django 4.2.1 on 2023-07-06 18:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('DatabaseEngine', '0012_employee_grade'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='verfied',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='Background_Verification',
            fields=[
                ('verification_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('verified_on', models.DateTimeField(auto_now=True)),
                ('verification_employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DatabaseEngine.employee')),
                ('verified_approved_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
