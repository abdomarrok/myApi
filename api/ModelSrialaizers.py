from rest_framework import serializers
from api.models import Restaurant

class RestaurantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Restaurant
        fields = ('name', 'address')