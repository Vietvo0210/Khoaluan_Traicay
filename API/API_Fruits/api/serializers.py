from rest_framework import serializers

from .models import Product,Customer,Feedback,Galery,Order_details,Orders

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'

class GalerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Galery
        fields = '__all__'

class OdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = '__all__'
class Order_detailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order_details
        fields = '__all__'