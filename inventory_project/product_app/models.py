#--------------Imports-------------------------------
from django.db import models

#-------------Models---------------------------------
# Model looks good. But few suggestions - 1. CATEGORY_CHOICES this way it has become the Class Data Members. Can be defined outside..
#                                       2. Add image to Product so that you can get familier with handling images.
#                                       3. MAke Category as seperate model to practice work on related data as well.
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
