# Generated by Django 5.0.4 on 2024-12-01 15:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transportation', '0068_alter_rented_cars_share_rates'),
    ]

    operations = [
        migrations.CreateModel(
            name='payment_process',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_reference', models.CharField(editable=False, max_length=20, unique=True, verbose_name='Transacton')),
                ('status', models.CharField(default='uncheck', max_length=50)),
                ('amount', models.IntegerField()),
                ('transaction_type', models.IntegerField(choices=[(1, 'Onsite'), (2, 'Online')], default=0)),
                ('category', models.CharField(max_length=50)),
                ('shop_processed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shoppayments', to='transportation.shops', verbose_name='Shop Payments')),
            ],
        ),
    ]
