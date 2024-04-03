from rest_framework import serializers
from app.model import CustomUser, Product, Manufacturer

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password')


class ManufacturerSerializer(serializers.ModelSerializer): 
    
    class Meta: 
        model = Manufacturer 
        fields = "__all__"

class ProductSerializer(serializers.ModelSerializer): 
    
    class Meta: 
        model = Product 
        fields = "__all__"