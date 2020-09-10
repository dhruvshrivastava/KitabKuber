# Generated by Django 3.1.1 on 2020-09-10 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_books_book_advance'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(max_length=1000)),
                ('book_ordered', models.CharField(max_length=1000)),
                ('customer_email', models.CharField(max_length=1000)),
                ('customer_name', models.CharField(max_length=1000)),
                ('customer_mobile', models.CharField(max_length=1000)),
                ('customer_line1', models.CharField(max_length=1000)),
                ('customer_line2', models.CharField(max_length=1000)),
                ('customer_city', models.CharField(max_length=1000)),
                ('customer_pincode', models.CharField(max_length=1000)),
            ],
        ),
    ]
