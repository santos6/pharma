# Generated by Django 5.1.3 on 2024-11-11 15:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Produits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('quantite', models.PositiveBigIntegerField(default=0)),
                ('description', models.TextField()),
                ('date_ajout', models.DateTimeField(auto_now_add=True)),
                ('date_expiration', models.DateField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Produits.categories')),
            ],
            options={
                'ordering': ['-date_ajout'],
            },
        ),
        migrations.CreateModel(
            name='Vente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sale_date', models.DateTimeField(auto_created=True)),
                ('quantite', models.PositiveBigIntegerField()),
                ('customer', models.CharField(max_length=100)),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('produit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Produits.produits')),
            ],
        ),
        migrations.CreateModel(
            name='Facture_Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantite', models.PositiveBigIntegerField()),
                ('date_achat', models.DateTimeField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Produits.customer')),
                ('produit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Produits.produits')),
                ('total_amount', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Produits.vente')),
            ],
        ),
    ]
