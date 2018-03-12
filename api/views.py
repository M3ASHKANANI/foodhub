from django.shortcuts import render

from rest_framework.generics import ListAPIView, RetrieveAPIView, DestroyAPIView, CreateAPIView, RetrieveUpdateAPIView
from restaurants.models import Restaurant
from .serializer import RestaurantListserializer , RestaurantDetailserializer, RestaurantCreateserializer
# Create your views here.

class RestaurantListAPIView(ListAPIView):
	queryset = Restaurant.objects.all()
	serializer_class = RestaurantListserializer


class RestaurantDetailAPIView(RetrieveAPIView):
	queryset = Restaurant.objects.all()
	serializer_class = RestaurantDetailserializer
	lookup_field = 'id'
	lookup_url_kwarg = 'rest_id'


class RestaurantDeleteAPIView(DestroyAPIView):
	queryset = Restaurant.objects.all()
	serializer_class = RestaurantDetailserializer
	lookup_field = 'id'
	lookup_url_kwarg = 'rest_id'


class RestaurantCreateAPIView(CreateAPIView):
	queryset = Restaurant.objects.all()
	serializer_class = RestaurantCreateserializer	

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)


class RestaurantUpdateAPIView(RetrieveUpdateAPIView):
	queryset = Restaurant.objects.all()
	serializer_class = RestaurantCreateserializer
	lookup_field = 'id'
	lookup_url_kwarg = 'rest_id'	


