from django.shortcuts import render
from .models import Restaurant

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