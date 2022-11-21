from rest_framework import serializers
from test_django.models import Empmodel
from test_django.models import ProductModel

class Serializationclass(serializers.ModelSerializer):
	class Meta:
		model=Empmodel
		fields= '__all__'


class ProductSerializationclass(serializers.ModelSerializer):
    class Meta:
        model=ProductModel
        fields='__all__'
