# Generated by Django 3.1.1 on 2020-09-10 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20200908_1859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='book_image',
            field=models.ImageField(blank=True, upload_to='uploads/'),
        ),
    ]
