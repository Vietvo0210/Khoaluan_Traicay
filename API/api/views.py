from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.http import JsonResponse
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from keras.models import load_model
import cv2
import numpy as np
import requests
from PIL import Image
import urllib.request
import skimage.io
from imaplib import _Authenticator
from .serializers import ProductSerializer,CustomerSerializer,FeedbackSerializer,GalerySerializer,Order_detailsSerializer,OdersSerializer
from .models import Product,Galery,Feedback,Order_details,Orders,Customer
from django.http import JsonResponse
from rest_framework.generics import ListCreateAPIView
from django.contrib.auth.models import User

# Create your views here.
# Product

@api_view(['GET'])
def ShowAll(request):
    products = Product.objects.all()[:10]
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def ViewProduct(request, pk):
    product = Product.objects.get(id=pk)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def CreateProduct(request):
    serializer = ProductSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)



@api_view(['POST'])
def updateProduct(request, pk):
    product = Product.objects.get(id=pk)
    serializer = ProductSerializer(instance=product, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['GET'])
def deleteProduct(request, pk):
    product = Product.objects.get(id=pk)
    product.delete()

    return Response('Items delete successfully!')

#Customer

@api_view(['GET'])
def ShowAll_Customer(request):
    customer = Customer.objects.all()[:10]
    serializer = CustomerSerializer(customer, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def ViewCustomer(request, pk):
    customer = Customer.objects.get(id=pk)
    serializer = CustomerSerializer(customer, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def CreateCustomer(request):
    serializer = CustomerSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)



@api_view(['POST'])
def updateCustomer(request, pk):
    customer = Customer.objects.get(id=pk)
    serializer = CustomerSerializer(instance=customer, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['GET'])
def deleteCustomer(request, pk):
    customer = Customer.objects.get(id=pk)
    customer.delete()

    return Response('Items delete successfully!')

#Feedback

@api_view(['GET'])
def ShowAll_Feedback(request):
    feedback = Feedback.objects.all()[:10]
    serializer = FeedbackSerializer(feedback, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def ViewFeedback(request, pk):
    feedback = Feedback.objects.get(id=pk)
    serializer = FeedbackSerializer(feedback, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def CreateFeedback(request):
    serializer = FeedbackSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)



@api_view(['POST'])
def updateFeedback(request, pk):
    feedback = Feedback.objects.get(id=pk)
    serializer = FeedbackSerializer(instance=feedback, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['GET'])
def deleteFeedback(request, pk):
    feedback = Feedback.objects.get(id=pk)
    feedback.delete()

    return Response('Items delete successfully!')


#Galery
@api_view(['GET'])
def ShowAll_Galery(request):
    galery = Galery.objects.all()[:10]
    serializer = GalerySerializer(galery, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def ViewGalery(request, pk):
    galery = Galery.objects.get(id=pk)
    serializer = GalerySerializer(galery, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def CreateGalery(request):
    serializer = GalerySerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)



@api_view(['POST'])
def updateGalery(request, pk):
    galery = Galery.objects.get(id=pk)
    serializer = GalerySerializer(instance=galery, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['GET'])
def deleteGalery(request, pk):
    galery = Galery.objects.get(id=pk)
    galery.delete()

    return Response('Items delete successfully!')

#Orders
@api_view(['GET'])
def ShowAll_Orders(request):
    orders = Orders.objects.all()[:10]
    serializer = OdersSerializer(orders, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def ViewOrders(request, pk):
    orders = Orders.objects.get(id=pk)
    serializer = OdersSerializer(orders, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def CreateOrders(request):
    serializer = OdersSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)



@api_view(['POST'])
def updateOrders(request, pk):
    orders = Orders.objects.get(id=pk)
    serializer = OdersSerializer(instance=orders, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['GET'])
def deleteOrders(request, pk):
    orders = Orders.objects.get(id=pk)
    orders.delete()

    return Response('Items delete successfully!')

#Order_details
@api_view(['GET'])
def ShowAll_Order_details(request):
    order_details = Order_details.objects.all()[:10]
    serializer = Order_detailsSerializer(order_details, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def Vieworder_details(request, pk):
    order_details = Order_details.objects.get(id=pk)
    serializer = Order_detailsSerializer(order_details, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def Createorder_details(request):
    serializer = Order_detailsSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)



@api_view(['POST'])
def updateorder_details(request, pk):
    order_details = Order_details.objects.get(id=pk)
    serializer = Order_detailsSerializer(instance=order_details, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['GET'])
def deleteorder_details(request, pk):
    order_details = Order_details.objects.get(id=pk)
    order_details.delete()

    return Response('Items delete successfully!')


def login(seft,request):
            email=request.POST['email']
            password = request.POST['password']
            bool_answer = User.objects.filter(yourtablefield="admin").exists()
            intakes = bool_answer.objects.all().filter(email,password)

            for intake in intakes:

                if intake.email==email and intake.password==password:
                     return True
                else:
                     return False



class GetPredictedResult(ListCreateAPIView):
    vgg16_model=load_model('/Users/admin/Desktop/Hocky6/Nhandangraucu_mayhoc/GUI/Viet_Huy_Doan_Traicay.model')
    class_names = ["ambarella", "avocado ", "banana", "coconut", "custardapple", "dragonfruit", "durian", "guava", "jackfruit" ,
                  "lychee","mango","mangosteen","persimmon","pineapple","plumcot",
                  "plums","pomelo", "rambutan","saboche","tomato", "watermelon"
                  ]
    def get(self,request):
        url = 'https://duockienminh.vn/sites/default/files/anh_bai_viet/1-la-du-du-la-gi-tai-sao-nhieu-ngu.jpg'
        # req = urllib.request.urlopen(url)
        # arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
        # image = cv2.imdecode(arr,1)
        image=skimage.io.imread('/Users/admin/Desktop/Validation_te??t/saurieng.jpeg')
        image_resized = cv2.resize(image,(224,224))
        image=np.expand_dims(image_resized,axis=0)
        pred = self.vgg16_model.predict(image)
        accuracy = float("{:.2f}".format(max(pred[0]))) * 100
        accuracy = int(accuracy)
        return JsonResponse({
                'Loai': ''+self.class_names[np.argmax(pred)],
            }, status=status.HTTP_201_CREATED)

