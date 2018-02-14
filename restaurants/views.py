from django.shortcuts import render, redirect
from .models import Restaurant
from .forms import RestaurantForm

def detail(request, rest_id):
	context = {
	"Restaurant": Restaurant.objects.get(id=rest_id)
	}
	return render(request, "hi.html", context)

def list(request):
	context = {
	"Restaurant": Restaurant.objects.all(),

	}
	return render(request, "Rest.html" , context)

def create(request):
	form = RestaurantForm()
	if request.method == "POST":
		form = RestaurantForm(request.POST)
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
		form = RestaurantForm(request.POST , instance=rest_obj)
		if form.is_valid():
			form.save()
			return redirect("rest_detail", rest_id=rest_obj.id)
	context = {
		"update_form":form,
		"rest_obj":rest_obj,

	}
	return render(request, "restaurant_update.html", context)

def delete(request, rest_id):
	rest.objects.get(id=rest_id).delete()
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