from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
# from .product import products
from django.contrib.auth.models import User

from base.models import Product
from base.serializers import ProductSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.hashers import make_password
from rest_framework import status


@api_view(['GET'])
def get_products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def get_product(request,pk):
    product = Product.objects.get(pk=pk)
    serializer = ProductSerializer(product, many = False)
    return Response(serializer.data)