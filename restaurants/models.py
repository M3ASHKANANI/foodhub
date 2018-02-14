from django.db import models

class Restaurant(models.Model):
	name = models.CharField(max_length = 30)
	description = models.TextField()
	opening_time = models.TimeField(auto_now_add=True)
	closing_time = models.TimeField(auto_now_add=True)

	def __str__(self):
		return self.name