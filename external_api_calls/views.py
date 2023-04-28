from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product
from rest_framework import status
from .serializers import ProductSerializer
import requests
import uuid


# Create your views here.

class CurdCurdApi(APIView):
    BaseURL = "https://crudcrud.com/api/3171a8f37b4a41fda901dd72e61e20e6/my_products"

    def post(self, request, *args, **kwargs):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = requests.post(self.BaseURL, json=serializer.data)

            print(response)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id=None, *arges, **kwargs):
        if id is None:
            response = requests.get(self.BaseURL)
            print(response)
            return Response(response, status=status.HTTP_200_OK)
        try:
            db_product_data = Product.objects.get(pk=id)
            serializer = ProductSerializer(db_product_data)
            print(serializer)
            return Response(serializer.data, status=status.HTTP_200_OK)
        finally:
            response = requests.get(self.BaseURL + "/" + id)
            return Response(response, status=status.HTTP_200_OK)

    def put(self, request, id=None, *args, **kwargs):
        if id is None:
            return Response({"details": "id required"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            product = Product.objects.get(id=id)
            serializer = ProductSerializer(instance=product, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                print("hei")
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        finally:
            response = requests.put(self.BaseURL, json=request.data)
            return Response(response, status=status.HTTP_201_CREATED)

    def delete(self, request, id=None):
        if id is None:
            return Response({"details": "id required"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            product = Product.objects.get(id=id)
            product.delete()
            return Response({"details": "deleted"}, status=status.HTTP_400_BAD_REQUEST)
        finally:
            response = requests.delete(self.BaseURL + "/" + id)
            return Response(response, status=status.HTTP_201_CREATED)
