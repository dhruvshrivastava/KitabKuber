from django.db import models


class Books(models.Model):
    book_name = models.CharField(max_length=1000)
    book_description = models.CharField(max_length=5000)
    book_image = models.ImageField(upload_to='catalog/', blank=True)
    book_price = models.FloatField()
    book_category = models.CharField(max_length=500)

    def __str__(self):
        return self.book_name
