from django.contrib import admin
from .models import Restaurant, Item, FavoriteRes, FavoriteItem
admin.site.register(Restaurant)
admin.site.register(Item)
admin.site.register(FavoriteRes)
admin.site.register(FavoriteItem)