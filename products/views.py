from django.shortcuts import render
from rest_framework import viewsets
from .models import Product, Categories
from .serializers import ProductSerializer, CategoriesSerializer
# Create your views here.

# CategoriesViewSet ==============================
class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
# ProductViewSet ==================================
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # function for filter product by name
    # def get_queryset(self):
    #     # name = self.request.query_params.get("name")
    #     return Product.objects.filter(name = self.request.query_params.get("name"))

    def perform_create(self, serializer):
        return super().perform_create(serializer)
# function for edit information of products
class EditProduct():
    pass