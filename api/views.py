from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.decorators import action
from .serializers import CategorySerializer, MaterialSerializer, UserSerializer, UserReviewSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from .permission import CustomPermissions
from .models import Category, Material, User, UserReview
from account.models import MyUser
import requests


class CategoryView(viewsets.ModelViewSet):
    permission_classes = [CustomPermissions]

    serializer_class = CategorySerializer
    queryset = Material.objects.all()
# class CustomCategoryView(viewsets.ReadOnlyModelViewSet):
#     queryset = Material.objects.all()
#     serializer_class = MaterialSerializer
#     lookup_field = "id"
#     @action(detail=True)
#     def category_list(self):
class SubCategoryView(viewsets.ModelViewSet):
    permission_classes = [CustomPermissions]

    serializer_class = MaterialSerializer
    queryset = Material.objects.all()


class CreateUser(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = MyUser.objects.all()


class CreateUserReview(viewsets.ModelViewSet):
    permission_classes = [CustomPermissions]

    serializer_class = UserReviewSerializer
    queryset = UserReview.objects.all()


# class CategoryView(APIView):
#     permission_classes = [CustomPermissions]
#
#     def get(self, request):
#         category = Category.objects.all()
#         serializer = CategorySerializer(category, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#
#     def post(self, request):
#
#         serializer = CategorySerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def put(self, request):
#         category = Category.objects.get(id=request.data.get("id"))
#         serializer = CategorySerializer(category, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request):
#         Category.objects.get(id=request.data.get("id")).delete()
#         return Response(status=status.HTTP_200_OK)
