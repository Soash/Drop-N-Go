# Generated by Django 4.0.6 on 2024-06-05 10:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shop', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='RequestedPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_profit', models.DecimalField(decimal_places=0, default=0, max_digits=15)),
                ('requested_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('invoice_number', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('orders', models.ManyToManyField(related_name='requested_payments', to='shop.order')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Reseller')),
            ],
        ),
        migrations.CreateModel(
            name='PaymentHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_profit', models.DecimalField(decimal_places=0, default=0, max_digits=15)),
                ('requested_date', models.DateTimeField()),
                ('invoice_number', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=20)),
                ('trxid', models.CharField(max_length=100)),
                ('reference', models.CharField(max_length=255)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('orders', models.ManyToManyField(to='shop.order')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Reseller')),
            ],
        ),
    ]
