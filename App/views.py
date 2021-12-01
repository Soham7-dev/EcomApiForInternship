from django.shortcuts import render
from rest_framework import serializers
from rest_framework.decorators import api_view
from .models import Category, Item
from .serializers import CategorySerializer, ItemSerializer
from rest_framework.response import Response
# Create your views here.


@api_view(['GET'])
def ReadCategories(request):
    serializer = CategorySerializer(Category.objects.all(), many=True)
    return Response(serializer.data)


@api_view(['GET'])
def ReadItems(request):
    serializer = ItemSerializer(Item.objects.all(), many=True)
    return Response(serializer.data)
