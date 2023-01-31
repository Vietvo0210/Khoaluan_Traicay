from rest_framework import serializers

from .models import Product,Customer,Feedback,Order_details,Orders,Image,News

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

class OdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = '__all__'
class Order_detailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order_details
        fields = '__all__'

class ImgSerializer(serializers.ModelSerializer):
    class Meta:
        model= Image
        fields=('file',)

class NewSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'
