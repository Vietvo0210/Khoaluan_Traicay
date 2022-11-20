from rest_framework import serializers
from test_django.models import Empmodel

class Serializationclass(serializers.ModelSerializer):
	class Meta:
		model=Empmodel
		fields= '__all__'