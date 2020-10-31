from django.db import models


class Books(models.Model):
    book_name = models.CharField(max_length=1000)
    book_description = models.CharField(max_length=5000)
    book_image = models.ImageField(upload_to='uploads/', blank=True)
    book_price = models.FloatField()
    book_category = models.CharField(max_length=500)
    book_advance = models.FloatField(default=0)
    

    def __str__(self):
        return self.book_name

class Orders(models.Model):
    rentalperiod = models.CharField(max_length=1000, default=0)
    deductible = models.CharField(max_length=1000, default=0)
    order_number = models.CharField(max_length=1000)
    book_ordered = models.CharField(max_length=1000)
    customer_email = models.CharField(max_length=1000)
    customer_name = models.CharField(max_length=1000)
    customer_mobile = models.CharField(max_length=1000)
    customer_line1= models.CharField(max_length=1000)
    customer_line2 = models.CharField(max_length=1000)
    customer_city = models.CharField(max_length=1000)
    customer_pincode = models.CharField(max_length=1000)
    def __str__(self):
        return self.order_number

class Sell(models.Model):
    name = models.CharField(max_length=1000, default=0)
    email = models.CharField(max_length=1000, default=0)
    mobile = models.CharField(max_length=1000, default=0)
    bookname = models.CharField(max_length=1000, default=0)
    bookpublisher = models.CharField(max_length=1000, default=0)
    book_image = models.ImageField(upload_to='uploads/', blank=True)
    def __str__(self):
        return self.bookname
   