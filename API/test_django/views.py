from test_django.serialization import Serializationclass, ProductSerializationclass
from test_django.models import Empmodel, ProductModel
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def ListAccount(request):
	if request.method=='GET':
		results=Empmodel.objects.all()
		serialize=Serializationclass(results, many=True)
		return Response(serialize.data)

@api_view(['GET'])
def ListProduct(request):
    if(request.method=='GET'):
        results= ProductModel.objects.all()
        serialize=ProductSerializationclass(results, many=True)
        return Response(serialize.data)
