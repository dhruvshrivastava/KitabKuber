# Generated by Django 3.1.1 on 2020-09-15 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_orders_rental'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orders',
            old_name='rental',
            new_name='rentalperiod',
        ),
        migrations.AddField(
            model_name='orders',
            name='deductible',
            field=models.CharField(default=0, max_length=1000),
        ),
    ]
