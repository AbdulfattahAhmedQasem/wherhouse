# Generated by Django 5.0.1 on 2024-02-27 09:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0009_joborderform_pdffile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='items_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='order',
            name='jobordernumber',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.joborderform'),
        ),
        migrations.AddField(
            model_name='order',
            name='total',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
        migrations.AlterField(
            model_name='joborderform',
            name='venueLocation',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='is_finished',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_details',
            field=models.ManyToManyField(through='orders.OrderDetails', to='orders.product'),
        ),
        migrations.AlterField(
            model_name='orderdetails',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.product'),
        ),
    ]
