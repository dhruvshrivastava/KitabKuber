# Generated by Django 3.1.1 on 2020-12-20 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0011_enquiry'),
    ]

    operations = [
        migrations.AddField(
            model_name='enquiry',
            name='email',
            field=models.CharField(default=0, max_length=1000),
        ),
        migrations.AddField(
            model_name='enquiry',
            name='mobile',
            field=models.CharField(default=0, max_length=1000),
        ),
        migrations.AddField(
            model_name='enquiry',
            name='name',
            field=models.CharField(default=0, max_length=1000),
        ),
    ]
