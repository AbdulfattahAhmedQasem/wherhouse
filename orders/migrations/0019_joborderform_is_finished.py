# Generated by Django 5.0.1 on 2024-03-07 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0018_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='joborderform',
            name='is_Finished',
            field=models.BooleanField(default=False),
        ),
    ]
