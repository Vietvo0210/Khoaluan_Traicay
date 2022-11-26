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

class Customer(models.Model):
    fullname = models.CharField(max_length=50)
    email = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    password = models.CharField(max_length=32)
    class Meta:
        db_table='Customer'

class Feedback(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    email = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=20)
    note = models.CharField(max_length=1000)
    class Meta:
        db_table='Feedback'

class Galery(models.Model):
    product_id = models.IntegerField()
    thumbnail = models.CharField(max_length=500)
    class Meta:
        db_table='Galery'

class Orders(models.Model):
    customer_id = models.IntegerField()
    fullname = models.CharField(max_length=50)
    email = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    note = models.CharField(max_length=1000)
    order_date=models.CharField(max_length=15)
    status=models.IntegerField()
    total_money=models.IntegerField()
    class Meta:
        db_table='Orders'

class Order_details(models.Model):
    order_id = models.IntegerField()
    product_id = models.IntegerField()
    price = models.IntegerField()
    num = models.IntegerField()
    total_money = models.IntegerField()
    class Meta:
        db_table='Order_details'
