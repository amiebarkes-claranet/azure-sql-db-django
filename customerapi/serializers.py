#Serializer for converting complex objects into native Python datatypes and deserialize parsed data back into complex types

from rest_framework import serializers
from customerapi.models import Customer,Product,OrderDetail, Equipment

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields=('CustomerId','CustomerName')

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product 
        fields=('ProductId','ProductName')

class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=OrderDetail
        fields=('OrderId','CustomerId','ProductId','OrderDate')

class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Equipment
        fields=('Equipment_ID','Plant_ID','Name','Description', 'WorkCenter', 'Department_Type', 'ValidUntil', 'CreatedAt', 'UpdatedAt', 'Enabled')