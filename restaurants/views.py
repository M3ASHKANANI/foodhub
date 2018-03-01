from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Restaurant ,FavoriteRes
from .forms import RestaurantForm ,UserRegisterForm
from django.contrib.auth import authenticate, login, logout


def detail(request, rest_id):
	restaurant_obj = Restaurant.objects.get(id=rest_id)
	item = Item.objects.filter(restaurant=restaurant_obj)
	context = {
	"Restaurant": restaurant_obj,
	"item": item,

	}
	return render(request, "hi.html", context)

def list(request):
	restaurant_list = Restaurant.objects.all()
	restaurant_list = restaurant_list.order_by("name", "publish_date")
	query = request.GET.get("q")
	if query:
		restaurant_list = restaurant_list.filter(name__contains=query)
	context = {
	"Restaurant": restaurant_list,

	}
	return render(request, "Rest.html" , context)

def create(request):
	form = RestaurantForm()
	if request.method == "POST":
		form = RestaurantForm(request.POST, request.FILES or None)
		if form.is_valid():
			form.save()
			return redirect("rest_list")
	context = {
		"create_form":form,
	}
	return render(request, "restaurant_create.html", context)

def create_item(request, rest_id):
	rest_obj = Restaurant.objects.get(id=rest_id)
	form = ItemForm()
	if request.method == "POST":
		form = ItemForm(request.POST, request.FILES or None)
		if form.is_valid():
			item = form.save(commit=False)
			item.restaurant = restaurant_obj
			item.save()
			return redirect("list")
	context = {
	"form":form,
	"rest_obj":rest_obj,

	}
	return render(request, "create_item", context)




def update(request , rest_id):
	rest_obj = Restaurant.objects.get(id=rest_id)
	form = RestaurantForm(instance=rest_obj)
	if request.method == "POST":
		form = RestaurantForm(request.POST , request.FILES or None, instance=rest_obj)
		if form.is_valid():
			form.save()
			return redirect("rest_detail", rest_id=rest_obj.id)
	context = {
		"update_form":form,
		"rest_obj":rest_obj,

	}
	return render(request, "restaurant_update.html", context)

def delete(request, rest_id):
	Restaurant.objects.get(id=rest_id).delete()
	return redirect("rest_list")

def register_user(request):
	form = UserRegisterForm()
	if request.method == "POST":
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			person = form.save(commit=False)
			person.set_password(person.password)
			person.save()
			login(request, person)
			return redirect("rest_list")
	context = {
		"create_form":form,
	}
	return render(request, "register.html", context)


def login_user(request):
	form = LoginForm()
	if request.method == "POST":
		form = LoginForm(request.POST)
		if form.is_valid():
			username = request.POST["username"]
			password = request.POST["password"]
			user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect("rest_list")


def logout_user(request):
	logout(request)
	return redirect("rest_list")

def favorite(request, rest_id):
	restaurant_obj = Restaurant.objects.get(id=rest_id)
	favorite_obj, created = FavoriteRes.objects.get_or_create(user=request.user, restaurant=restaurant_obj)
	if created:
		action="favorite"
	else:
		action="unfavorite"
		favorite_obj.delete()
	favorite_count = restaurant_obj.favoriteres_set.all().count()
	# favorite_count = FavoriteRes.objects.filter(restaurant=restaurant_obj)

	context = {
	"action": action,
	"count": favorite_count,
	
	}
	return JsonResponse(context, safe=False)


# def list(request):
# 	context = {
# 	"XYZ": [
# 	{"restaurants" : "RHS",
# 	"menu": "Burgers",
# 	"price_range" : "$$"},
# 	{"restaurants" : "subway",
# 	"menu": "healthy food",
# 	"price_range" : "$"},
# 	{"restaurants" : "joy",
# 	"menu": "sweet",
# 	"price_range" : "$$$"},
# 	]
# 	}
# 	return render(request, "Rest.html", context)