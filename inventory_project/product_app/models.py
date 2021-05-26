#--------------Imports-------------------------------
from django.db import models

#-------------Models---------------------------------
class Product(models.Model):
    ELECTRONICS = 'EL'
    FASHION = 'FA'
    BOOKS = 'BO'
    CLEANING = 'CL'
    BEAUTY = 'BE'
    CATEGORY_CHOICES = [
        (ELECTRONICS, 'Electronics'),
        (FASHION, 'Fashion'),
        (BOOKS, 'Books'),
        (CLEANING, 'Cleaning'),
        (BEAUTY, 'Beauty'),
    ]

    name = models.CharField(max_length=30)
    category = models.CharField(
        max_length=2,
        choices=CATEGORY_CHOICES,
    )
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)


    def __str__(self):
        return self.name 
