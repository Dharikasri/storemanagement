# Generated by Django 5.0.6 on 2024-06-10 12:59

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.IntegerField(unique=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('expiry_date', models.DateField(null=True)),
                ('price', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10)),
                ('categories', models.ManyToManyField(related_name='products', to='category.category')),
            ],
        ),
    ]
