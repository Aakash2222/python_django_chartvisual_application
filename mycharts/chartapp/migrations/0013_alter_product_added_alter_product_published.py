# Generated by Django 4.0.2 on 2024-03-02 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chartapp', '0012_alter_product_insight'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='added',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='published',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]