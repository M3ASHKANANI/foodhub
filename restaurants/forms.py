from django import forms
from .models import Restaurant

class RestaurantForm(forms.ModelForm):
	class Meta:
		model = Restaurant
		fields = "__all__"

		widgets = {
			"publish_date": forms.DateInput(attrs={"type":"data"})
		}