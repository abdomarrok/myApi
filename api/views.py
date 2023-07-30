from django.shortcuts import render
from rest_framework import viewsets
from api.ModelSrialaizers import RestaurantSerializer
from api.models import Restaurant

class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
   

