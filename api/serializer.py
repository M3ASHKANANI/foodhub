from rest_framework import serializers
from restaurants.models import Restaurant, FavoriteRes, FavoriteItem, Item
from django.contrib.auth.models import User
from rest_framework_jwt.settings import api_settings

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ["username", "first_name", "last_name"]

class RestaurantListserializer(serializers.ModelSerializer):
	detail_page = serializers.HyperlinkedIdentityField(
		view_name = "api-detail",
		lookup_field = "id",
		lookup_url_kwarg = "rest_id"
		)
	# owner = serializers.SerializerMethodField()
	owner = UserSerializer()
	class Meta:
		model = Restaurant
		fields=["id", "name", "description","owner","detail_page"]

	def get_owner(self, obj):
			return obj.owner.username

class RestaurantDetailserializer(serializers.ModelSerializer):
	favorites = serializers.SerializerMethodField()
	items = serializers.SerializerMethodField()

	owner = UserSerializer()

	delete_page = serializers.HyperlinkedIdentityField(
		view_name = "api-delete",
		lookup_field = "id",
		lookup_url_kwarg = "rest_id"
		)
	update_page = serializers.HyperlinkedIdentityField(
		view_name = "api-update",
		lookup_field = "id",
		lookup_url_kwarg = "rest_id"
		)
		
	class Meta:
		model = Restaurant
		fields=["name", "description", "image"]

	def get_owner(self, obj):
		return obj.owner.username

	def get_favorites(self, obj):
		favorites = obj.favoriteres_set.all()
		json_favorite = FavoriteListSerializer(favorites, many=True).data
		return json_favorite

	def get_items(self, obj):
		items = obj.item_set.all()
		json_items = ItemListserializer(items, many=True).data
		return json_favorite


class RestaurantCreateserializer(serializers.ModelSerializer):
	class Meta:
		model = Restaurant
		fields = ["name", "description", "image"]


class RestaurantDetailSerializer(serializers.ModelSerializer):
	favorite = serializers.SerializerMethodField()

	class Meta:
		model = Restaurant
		fields = ["id", "name", "description", "owner", "publish_date", "favorite"]

	def get_Favorite(self, obj):
		# likes = Favorite.objects.filter(restaurant=obj)
		favorite = obj.favorite_set.all()
		json_favorite = FavoriteListSerializer(favorite, many=True).data
		return json_favorite

class FavoriteCreateSerializer(serializers.ModelSerializer):
	class Meta:
		model = FavoriteRes
		fields = ["restaurant"]


class FavoriteListSerializer(serializers.ModelSerializer):
	user = UserSerializer()

	class Meta:
		model = FavoriteRes
		fields = ["user"]

class ItemCreateserializer(serializers.ModelSerializer):
	class Meta:
		model = Item
		fields = ["restaurant", "name", "price"]

class ItemListserializer(serializers.ModelSerializer):
	detail_page = serializers.HyperlinkedIdentityField(
		view_name = "api-list-item",
		lookup_field = "id",
		lookup_url_kwarg = "rest_id"
		)
	# owner = serializers.SerializerMethodField()
	owner = UserSerializer()
	class Meta:
		model = Item
		fields=["id", "restaurant", "name","description","price"]


class RegisterUserSerializer(serializers.ModelSerializer):
	password = serializers.CharField(style={"input_type":"password"}, write_only=True)
	class Meta:
		model = User
		fields = ["username", "first_name", "last_name", "email", "password"]

	def create(self, validated_data):
		new_user = User(**validated_data)
		new_user.set_password(validated_data["password"])
		new_user.save()
		return validated_data


class UserLoginSerializer(serializers.Serializer):
	username = serializers.CharField()
	password = serializers.CharField(style={"input_type":"password"}, write_only=True)
	token = serializers.CharField(allow_blank=True, read_only=True)

	def validate(self, data):
		my_username = data.get("username")
		my_password = data.get("password")


		if my_username == "":
			raise serializers.ValidationError("A username is required to login")

		# user = User.objects.fillter(username=my_username)
		# if user.exists():
		# 	user_obj = user.first()
		# else:
		# 	raise serializers.ValidationError("This username does not exist")


		try:
			user_obj = User.objects.get(username=my_username)
		except:
			raise serializers.ValidationError("This username does not exist")

		if not user_obj.check_password(my_password):
			raise serializers.ValidationError("Incorrect username/password combination")

		jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
		jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

		payload = jwt_payload_handler(user_obj)
		token = jwt_encode_handler(payload)

		data["token"] = token
		return data