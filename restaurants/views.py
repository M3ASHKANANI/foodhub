from django.shortcuts import render

def detail(request):
	context = {
	"title": "some random article",
	"content": "There is some content here",
	"created": "8-02-2018",
	"updated": "08-02-2018",
	}
	return render(request, "hi.html", context)

def list(request):
	context = {
	"XYZ": [
	{"restaurants" : "RHS",
	"menu": "Burgers",
	"price_range" : "$$"},
	{"restaurants" : "subway",
	"menu": "healthy food",
	"price_range" : "$"},
	{"restaurants" : "joy",
	"menu": "sweet",
	"price_range" : "$$$"},
	]
	}
	return render(request, "Rest.html", context)