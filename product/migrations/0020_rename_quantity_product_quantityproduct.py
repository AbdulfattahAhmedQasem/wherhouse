# Generated by Django 5.0.1 on 2024-03-10 14:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0019_alter_product_productheight_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='quantity',
            new_name='quantityproduct',
        ),
    ]
