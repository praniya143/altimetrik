from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import filters
import jwt
from django.conf import settings
from datetime import datetime, timedelta

from django.contrib.auth import authenticate
from app.serializer import UserSerializer, ProductSerializer, ManufacturerSerializer
from app.model import Product, Manufacturer

class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

def generate_jwt_token(user_id):
    payload = {
        'user_id': user_id,
        'exp': datetime.utcnow() + timedelta(days=1)  # Token expiration time
    }
    jwt_token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
    return jwt_token.decode('utf-8')

class UserLoginView(APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request):
        user = authenticate(username=request.data['username'], password=request.data['password'])
        if user:
            token = generate_jwt_token(user.id)
            return Response({'token': token})
        else:
            return Response({'error': 'Invalid credentials'}, status=401)

class ManufacturerBase():
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer

class ManufacturerListCreateView(ManufacturerBase, generics.ListCreateAPIView):
    pass
    
    
class ManufacturerDetailView(ManufacturerBase, generics.RetrieveUpdateDestroyAPIView):
    pass
    
class AllManufacturersListView(ManufacturerBase, generics.ListAPIView):
    filter_backends = [filters.SearchFilter]
    
class ManufacturerUpdateView(ManufacturerBase, generics.RetrieveUpdateAPIView):
    partial = True
    
    
class ManufacturerDeleteView(ManufacturerBase, generics.DestroyAPIView):
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(print("delete Manufacturer"))

class ProductBase():
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductListCreateView(ProductBase, generics.ListCreateAPIView):
    pass
        
class ProductDetailView(ProductBase, generics.RetrieveUpdateDestroyAPIView):
    pass
    
class AllProductsListView(ProductBase, generics.ListAPIView):
    filter_backends = [filters.SearchFilter]
    
class ProductUpdateView(ProductBase, generics.RetrieveUpdateAPIView):
    partial = True
    
    
class ProductDeleteView(ProductBase, generics.DestroyAPIView):
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(print("delete Product"))
