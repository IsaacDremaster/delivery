# Generated by Django 3.2 on 2021-04-30 14:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20210430_2001'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('order', '0003_auto_20210430_2001'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profiles',
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL),
        ),
    ]
