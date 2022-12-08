from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import ProductSerializer
from .models import Product

from django.shortcuts import render
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



# Create your views here.

"""@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/product-list/',
        'Detail View': '/product-detail/<int:id>/',
        'Create': '/product-create/',
        'Update': '/product-update/<int:id>/',
        'Delete': '/product-detail/<int:id>/',
    }
    return Response(api_urls);
"""

@api_view(['GET'])
def ShowAll(request):
    products = Product.objects.all()
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



@api_view(['PUT'])
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

class GetPredictedResult(ListCreateAPIView):
    vgg16_model=load_model('E:/huyvip_123/KhoaLuan_NhanDangHoaQua/Viet_Huy_Doan_Traicay/Viet_Huy_Doan_Traicay.model')
    class_names = ["ambarella", "avocado ", "banana", "coconut", "custardapple", "dragonfruit", "durian", "guava", "jackfruit" ,
                  "lychee","mango","mangosteen","persimmon","pineapple","plumcot",
                  "plums","pomelo", "rambutan","saboche","tomato", "watermelon"
                  ]
    def get(self,request):
        url = 'https://duockienminh.vn/sites/default/files/anh_bai_viet/1-la-du-du-la-gi-tai-sao-nhieu-ngu.jpg'
        # req = urllib.request.urlopen(url)
        # arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
        # image = cv2.imdecode(arr,1)
        image=skimage.io.imread('/Users/admin/Desktop/Validation_tét/saurieng.jpeg')
        image_resized = cv2.resize(image,(224,224))
        image=np.expand_dims(image_resized,axis=0)
        pred = self.vgg16_model.predict(image)
        accuracy = float("{:.2f}".format(max(pred[0]))) * 100
        accuracy = int(accuracy)
        return JsonResponse({
                'Loai': ''+self.class_names[np.argmax(pred)],
            }, status=status.HTTP_201_CREATED)

