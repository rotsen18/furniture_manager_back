# Generated by Django 4.0.8 on 2022-11-19 18:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('configurator', '0001_initial'),
        ('order', '0001_initial'),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='set',
            name='frame',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.product'),
        ),
        migrations.AddField(
            model_name='place',
            name='additional',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='additional', to='product.product'),
        ),
        migrations.AddField(
            model_name='place',
            name='cover',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cover', to='product.product'),
        ),
        migrations.AddField(
            model_name='place',
            name='mechanism',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mech', to='product.product'),
        ),
        migrations.AddField(
            model_name='place',
            name='set',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='places', to='configurator.set'),
        ),
        migrations.AddField(
            model_name='orderset',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.order'),
        ),
        migrations.AddField(
            model_name='orderset',
            name='set',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configurator.set'),
        ),
    ]