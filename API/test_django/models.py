from django.db import models

class Empmodel(models.Model):
	email=models.CharField(max_length=100)
	name=models.CharField(max_length=100)
	password=models.CharField(max_length=100)
	class Meta:
		db_table='Admin'

class ProductModel(models.Model):
    title=models.CharField(max_length=100)
    price=models.IntegerField()
    class Meta:
        db_table='Product'
