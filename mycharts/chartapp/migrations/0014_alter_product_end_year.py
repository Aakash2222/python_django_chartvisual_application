# Generated by Django 4.0.2 on 2024-03-03 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chartapp', '0013_alter_product_added_alter_product_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='end_year',
            field=models.IntegerField(blank=True, max_length=100, null=True),
        ),
    ]