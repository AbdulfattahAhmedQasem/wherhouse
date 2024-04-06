# Generated by Django 5.0.1 on 2024-03-10 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0016_product_shapeproduct_product_typeproduct'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='productheight',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='productlength',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='productwidth',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
    ]
