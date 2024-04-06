# Generated by Django 5.0.1 on 2024-02-24 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_alter_order_order_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='jobOrderForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numberproject', models.IntegerField()),
                ('date', models.DateField()),
                ('jobOrderType', models.CharField(choices=[('sample', 'عينة'), ('rent', 'إيجار'), ('sale', 'بيع')], max_length=100)),
                ('clientName', models.CharField(max_length=100)),
                ('coordination', models.CharField(max_length=100)),
                ('projectManager', models.CharField(max_length=100)),
                ('venueLocation', models.CharField()),
                ('installationDate', models.DateField()),
                ('installationTime', models.TimeField()),
                ('openingDate', models.DateField()),
                ('openingTime', models.TimeField()),
                ('dismantleDate', models.DateField()),
                ('dismantleTime', models.TimeField()),
                ('handOverDateTime', models.DateTimeField()),
                ('note', models.CharField(max_length=250)),
            ],
        ),
    ]
