from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', UserLoginView.as_view()),
    path('manufacturers/', ManufacturerListCreateView.as_view(), name='Manufacturer-list-create'),
    path('manufacturers/<int:pk>/', ManufacturerDetailView.as_view(), name='Manufacturer-detail'),
    path('manufacturers/all/', ManufacturerListCreateView.as_view(), name='all-Manufacturers-list'),  
    path('manufacturers/delete/<int:pk>/', ManufacturerDeleteView.as_view(), name='Manufacturer-delete'), 
    path('manufacturers/update/<int:pk>/', ManufacturerUpdateView.as_view(), name='Manufacturer-update'), 
    path('product/', ProductListCreateView.as_view(), name='Product-list-create'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='Product-detail'),
    path('product/all/', ProductListCreateView.as_view(), name='all-Products-list'),  
    path('product/delete/<int:pk>/', ProductDeleteView.as_view(), name='Product-delete'), 
    path('product/update/<int:pk>/', ProductUpdateView.as_view(), name='Product-update'), 
    
]
