from django.shortcuts import render

from rest_framework.generics import ListAPIView, RetrieveAPIView, DestroyAPIView, CreateAPIView, RetrieveUpdateAPIView
from restaurants.models import Restaurant, FavoriteRes, FavoriteItem, Item
from .serializer import RestaurantListserializer , RestaurantDetailserializer, RestaurantCreateserializer,FavoriteCreateSerializer, ItemCreateserializer, ItemListserializer, RegisterUserSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from .permissions import IsOwnerOrStaff
from rest_framework.filters import SearchFilter, OrderingFilter
from django.contrib.auth.models import User
# Create your views here.

class RestaurantListAPIView(ListAPIView):
	queryset = Restaurant.objects.all()
	serializer_class = RestaurantListserializer
	permission_classes = [AllowAny]
	filter_backends = [SearchFilter,OrderingFilter]
	search_fields = ["name", "description", "owner__username", "id"]


class RestaurantDetailAPIView(RetrieveAPIView):
	queryset = Restaurant.objects.all()
	serializer_class = RestaurantDetailserializer
	lookup_field = 'id'
	lookup_url_kwarg = 'rest_id'
	permission_classes = [AllowAny]


class RestaurantDeleteAPIView(DestroyAPIView):
	queryset = Restaurant.objects.all()
	serializer_class = RestaurantDetailserializer
	lookup_field = 'id'
	lookup_url_kwarg = 'rest_id'
	permission_classes = [IsAuthenticated,IsOwnerOrStaff]


class RestaurantCreateAPIView(CreateAPIView):
	queryset = Restaurant.objects.all()
	serializer_class = RestaurantCreateserializer	

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)
		permission_classes = [IsAuthenticated]

class RestaurantUpdateAPIView(RetrieveUpdateAPIView):
	queryset = Restaurant.objects.all()
	serializer_class = RestaurantCreateserializer
	lookup_field = 'id'
	lookup_url_kwarg = 'rest_id'	
	permission_classes = [IsAuthenticated, IsOwnerOrStaff]

class FavoriteCreateView(CreateAPIView):
	queryset = FavoriteRes.objects.all()
	serializer_class = FavoriteCreateSerializer
	permission_classes = [IsAuthenticated,]

	def perform_create(self, serializer):
		serializer.save(user=self.request.user)


class ItemCreateAPIView(CreateAPIView):
	queryset = Item.objects.all()
	serializer_class = ItemCreateserializer	

	# def perform_create(self, serializer):
	# 	serializer.save(owner=self.request.user)
	# 	permission_classes = [IsAuthenticated]

class ItemListAPIView(ListAPIView):
	queryset = Item.objects.all()
	serializer_class = ItemListserializer
	permission_classes = [AllowAny]
	filter_backends = [SearchFilter,OrderingFilter]
	search_fields = ["name", "restaurant", "owner__username", "id"]


class UserRegisterView(CreateAPIView):
	queryset = User.objects.all()
	serializer_class = RegisterUserSerializer
	permission_classes = [AllowAny]



