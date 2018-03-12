from rest_framework import serializers
from restaurants.models import Restaurant

class RestaurantListserializer(serializers.ModelSerializer):
	class Meta:
		model = Restaurant
		fields=["id", "name", "description"]

class RestaurantDetailserializer(serializers.ModelSerializer):
	class Meta:
		model = Restaurant
		fields="__all__"



class RestaurantCreateserializer(serializers.ModelSerializer):
	class Meta:
		model = Restaurant
		fields = ["name", "description", "image"]