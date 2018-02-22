from django.shortcuts import render, redirect
from .models import Restaurant
from .forms import RestaurantForm ,UserRegisterForm
from django.contrib.auth import authenticate, login, logout

def detail(request, rest_id):
	context = {
	"Restaurant": Restaurant.objects.get(id=rest_id)
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