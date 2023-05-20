# Generated by Django 4.2.1 on 2023-05-20 17:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('catalogue', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlaceSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.IntegerField(default=1)),
                ('frame', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='catalogue.product')),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('additional', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='additional', to='catalogue.product')),
                ('cover', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cover', to='catalogue.product')),
                ('mechanism', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mech', to='catalogue.product')),
                ('set', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='places', to='configurator.placeset')),
            ],
        ),
    ]
