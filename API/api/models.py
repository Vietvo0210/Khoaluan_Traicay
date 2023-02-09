from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=250)
    price = models.FloatField()
    discount = models.IntegerField()
    thumbnail =models.CharField(max_length=500)
    description =models.CharField(max_length=2000)
    Vietnamesespecialfruit=models.BooleanField()
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
    fullname = models.CharField(max_length=30)
    email = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=20)
    note = models.CharField(max_length=1000)
    class Meta:
        db_table='Feedback'


class Orders(models.Model):
    fullname = models.CharField(max_length=50)
    email = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    note = models.CharField(max_length=1000)
    order_date=models.CharField(max_length=100)
    total_money=models.FloatField()
    class Meta:
        db_table='Orders'

class Order_details(models.Model):
    order_id = models.IntegerField()
    product_id = models.IntegerField()
    price = models.IntegerField()
    num = models.IntegerField()
    total_money = models.FloatField()
    class Meta:
        db_table='Order_details'

class Image(models.Model):
    file=models.ImageField(upload_to='media', null=False, default=None)
    class Meta:
        db_table='Image'

class News(models.Model):
    maTT =models.CharField(max_length=50)
    Thongtin = models.TextField()
    Hinh = models.CharField(max_length=50)
    Ngaydang = models.DateField()
    class Meta:
        db_table='News'

class Admin(models.Model):
    fullname = models.CharField(max_length=50)
    email = models.CharField(max_length=150)
    password = models.CharField(max_length=32)
    class Meta:
        db_table='Admin'