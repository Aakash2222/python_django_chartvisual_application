# Generated by Django 4.0.2 on 2024-03-01 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chartapp', '0006_product_category_product_num_of_products'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='end_year',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
