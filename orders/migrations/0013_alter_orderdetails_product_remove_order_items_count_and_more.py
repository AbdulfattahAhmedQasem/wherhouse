# Generated by Django 5.0.1 on 2024-02-27 10:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0012_alter_order_jobordernumber'),
        ('product', '0013_remove_product_publish_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderdetails',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product'),
        ),
        migrations.RemoveField(
            model_name='order',
            name='items_count',
        ),
        migrations.RemoveField(
            model_name='order',
            name='total',
        ),
        migrations.AlterField(
            model_name='joborderform',
            name='venueLocation',
            field=models.CharField(),
        ),
        migrations.AlterField(
            model_name='order',
            name='is_finished',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_details',
            field=models.ManyToManyField(through='orders.OrderDetails', to='product.product'),
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
