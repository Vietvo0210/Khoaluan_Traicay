from test_django.serialization import Serializationclass
from test_django.models import Empmodel
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def ListAccount(request):
	if request.method=='GET':
		results=Empmodel.objects.all()
		serialize=Serializationclass(results, many=True)
		return Response(serialize.data)
