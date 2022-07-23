# Generated by Django 4.0.5 on 2022-07-23 17:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('configurator', '0002_alter_place_set'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='additional',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='additional', to='configurator.product'),
        ),
        migrations.AlterField(
            model_name='place',
            name='cover',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cover', to='configurator.product'),
        ),
        migrations.AlterField(
            model_name='place',
            name='mechanism',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mech', to='configurator.product'),
        ),
    ]
