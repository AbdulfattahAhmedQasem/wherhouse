# Generated by Django 5.0.1 on 2024-02-18 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_yourmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yourmodel',
            name='field1',
            field=models.CharField(db_column='field1\xa0', max_length=255),
        ),
        migrations.AlterField(
            model_name='yourmodel',
            name='field2',
            field=models.IntegerField(db_column='field2\xa0'),
        ),
    ]