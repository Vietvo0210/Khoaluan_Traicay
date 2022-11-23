from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=250)
    price = models.IntegerField()
    discount = models.IntegerField()
    thumbnail =models.CharField(max_length=500)
    description =models.CharField(max_length=2000)
    class Meta:
        db_table='Product'
