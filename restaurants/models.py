from django.db import models
from django.contrib.auth.models import User

class Restaurant(models.Model):
	name = models.CharField(max_length = 30)
	description = models.TextField()
	image = models.ImageField(null=True)
	opening_time = models.TimeField(auto_now_add=True)
	closing_time = models.TimeField(auto_now_add=True)
	publish_date = models.DateField(null=True)


class Item(models.Model):
	restaurant = models.ForeignKey(Restaurant, default=1, on_delete=models.CASCADE)
	name = models.CharField(max_length=200)
	description = models.TextField()
	price = models.DecimalField(max_digits=7, decimal_places=3)

	def __str__(self):
		return self.name

class FavoriteRes(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

class FavoriteItem(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	item = models.ForeignKey(Item, on_delete=models.CASCADE)