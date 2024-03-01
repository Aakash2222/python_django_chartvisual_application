# Generated by Django 4.0.2 on 2024-03-01 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chartapp', '0005_remove_product_category_remove_product_end_year_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(default='', max_length=100, unique=True),
        ),
        migrations.AddField(
            model_name='product',
            name='num_of_products',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]