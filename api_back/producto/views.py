from django.shortcuts import render
from rest_framework import generics
from .models import Producto
from .serializers import ProductoSerializer

class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer