# Generated by Django 5.0.1 on 2024-02-29 11:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0015_alter_joborderform_numberproject_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='order_details',
        ),
    ]
