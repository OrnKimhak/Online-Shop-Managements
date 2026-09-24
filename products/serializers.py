from rest_framework import serializers
from .models import Product, Categories


# Categories Serializer ================================
class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'
# Product Serializer ================================
class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


    # Change categories number to name of categories
    # categories = serializers.ReadOnlyField(source = "categories.name")