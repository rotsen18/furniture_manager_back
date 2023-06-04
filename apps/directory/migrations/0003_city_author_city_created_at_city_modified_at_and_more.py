# Generated by Django 4.2.1 on 2023-06-04 09:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import furniture_manager.middlewares


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('directory', '0002_country_code_alter_city_name_alter_country_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='author',
            field=models.ForeignKey(
                default=furniture_manager.middlewares.get_current_authenticated_user,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name='city',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='city',
            name='modified_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='country',
            name='author',
            field=models.ForeignKey(
                default=furniture_manager.middlewares.get_current_authenticated_user,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name='country',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='country',
            name='modified_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]