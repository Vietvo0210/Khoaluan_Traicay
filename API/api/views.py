from rest_framework.response import Response
from rest_framework.decorators import api_view
from twilio.rest import Client
from .serializers import *
from .models import *
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver


from rest_framework import status
from django.http import JsonResponse
from rest_framework.generics import ListCreateAPIView


## import lbr load model
from keras.models import load_model

import cv2
import numpy as np
import skimage.io
from .serializers import NewSerializer,ProductSerializer,CustomerSerializer,FeedbackSerializer,Order_detailsSerializer,OdersSerializer,AdminSerializer
from .models import Product,Feedback,Order_details,Orders,Customer,News,Admin
from django.http import JsonResponse
from rest_framework.generics import ListCreateAPIView
import os
# Create your views here.

#New
@api_view(['GET'])
def NewList(request):
    news = News.objects.all()
    serializer = NewSerializer(news, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def CreateNew(request):
    serializer = NewSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    else:
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
# Product

@api_view(['GET'])
def ShowAll(request):
    products = Product.objects.all()[:8]
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

        return Response(serializer.data,status=status.HTTP_201_CREATED)
    else:
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)



@api_view(['PUT'])
def updateProduct(request, pk):
    product = Product.objects.get(id=pk)
    serializer = ProductSerializer(instance=product, data=request.data)
    if serializer.is_valid():
        serializer.save()

        return Response(serializer.data)
    else:
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def deleteProduct(request, pk):
    product = Product.objects.get(id=pk)
    product.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)



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
    else:
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def updateCustomer(request, pk):
    customer = Customer.objects.get(id=pk)
    serializer = CustomerSerializer(instance=customer, data=request.data)
    if serializer.is_valid():
        serializer.save()

        return Response(serializer.data)
    else:
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

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
    else:
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def updateFeedback(request, pk):
    feedback = Feedback.objects.get(id=pk)
    serializer = FeedbackSerializer(instance=feedback, data=request.data)
    if serializer.is_valid():
        serializer.save()

        return Response(serializer.data)
    else:
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def deleteFeedback(request, pk):
    feedback = Feedback.objects.get(id=pk)
    feedback.delete()

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
    else:
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def updateOrders(request, pk):
    orders = Orders.objects.get(id=pk)
    serializer = OdersSerializer(instance=orders, data=request.data)
    if serializer.is_valid():
        serializer.save()

        return Response(serializer.data)
    else:
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

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
    return Response(serializer.data,request)


@api_view(['POST'])
def Createorder_details(request):
    serializer = Order_detailsSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

        return Response(serializer.data)
    else:
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def updateorder_details(request, pk):
    order_details = Order_details.objects.get(id=pk)
    serializer = Order_detailsSerializer(instance=order_details, data=request.data)
    if serializer.is_valid():
        serializer.save()

        return Response(serializer.data)
    else:
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def deleteorder_details(request, pk):
    order_details = Order_details.objects.get(id=pk)
    order_details.delete()

    return Response('Items delete successfully!')

@receiver(pre_delete, sender=Image)
def mymodel_delete(sender, instance, **kwargs):
    instance.file.delete(False)

class GetPredictedResult(ListCreateAPIView):
    vgg16_model=load_model('/Users/admin/Desktop/Hocky6/Nhandangraucu_mayhoc/GUI/Viet_Huy_Doan_Traicay.model')
    class_names = ["ambarella", "avocado ", "banana", "coconut", "custardapple", "dragonfruit", "durian", "guava", "jackfruit" ,
                  "lychee","mango","mangosteen","persimmon","pineapple","plumcot",
                  "plums","pomelo", "rambutan","saboche","tomato", "watermelon"
                  ]
    def post(self,request):
        #delete old img
        Image.objects.all().delete()
        #post new img
        images = request.FILES['FILE']
        Image.objects.create(file=images)
        folder = './media/media'
        list = []
        for filename in os.listdir(folder):
            pathImg = 'http://127.0.0.1:8080/media/media/' + filename
            img = skimage.io.imread(os.path.join(folder, filename))

            image_resized = cv2.resize(img,(224,224))
            image=np.expand_dims(image_resized,axis=0)
            pred = self.vgg16_model.predict(image)
            accuracy = float("{:.2f}".format(max(pred[0]))) * 100
            accuracy = int(accuracy)
            result = {"type": self.class_names[np.argmax(pred)], "acc": accuracy, "image": pathImg}
            list.append(result)

        return JsonResponse(list, status=status.HTTP_201_CREATED, safe=False, json_dumps_params={'ensure_ascii': False})

@api_view(['GET'])
def CheckLogin(request, pk,gk):
    admin = Admin.objects.get(email=pk ,password=gk)
    serializer = AdminSerializer(admin, many=False)
    return Response(serializer.data,status=status.HTTP_200_OK)



@api_view(['GET'])
def SearchProduct(request,title):
    if(title.isdigit()):
        product=Product.objects.filter(price=title)
    else:
         product=Product.objects.filter(title__icontains=title)
    serializer=ProductSerializer(product,many=True)
    return Response(serializer.data)

#OTP
@api_view(['POST'])
def sendOTP(request):
    account_sid = "AC076f02360fc3d2b87ea9806cab108be0"
    auth_token = "08d6e8b1a21f12261ffee43e339f4b2b"
    verify_sid="VA462db428ceddbf93cefae70888e0d69c"
    client = Client(account_sid, auth_token)
    client.verify.services(verify_sid).verifications.create(
        to=f"+84{985357111}",
        channel="sms"
    )
    return Response(status=status.HTTP_200_OK)


@api_view(['POST'])
def verifyOTP(request):
    otp= request.POST.get("otp")
    account_sid = "AC076f02360fc3d2b87ea9806cab108be0"
    auth_token = "08d6e8b1a21f12261ffee43e339f4b2b"
    verify_sid="VA462db428ceddbf93cefae70888e0d69c"
    client = Client(account_sid, auth_token)
    print(otp)
    client.verify.services(verify_sid).verification_checks.create(
        to="+84985357111",
        code=otp
    )
    return Response(status=status.HTTP_200_OK)

# create acc admin
@api_view(['POST'])
def CreateAdmin(request):
    serializer = AdminSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

        return Response(serializer.data)
    else:
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def Vietnamesespecialtyfruit(request):
    products = Product.objects.filter(Vietnamesespecialfruit=bool(True))
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)