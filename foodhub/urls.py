"""foodhub URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from restaurants import views
from django.conf import settings
from django.conf.urls.static import static

from api.views import RestaurantListAPIView, RestaurantDetailAPIView , RestaurantDeleteAPIView, RestaurantCreateAPIView, RestaurantUpdateAPIView


urlpatterns = [
    path('admin/', admin.site.urls),
    path("hi/<int:rest_id>/", views.detail , name="rest_detail"),
    path("restaurants/",views.list ,name="rest_list"),
    path("create/",views.create, name="restaurant_create"),
    path("update/<int:rest_id>/", views.update, name="restaurant_update"),
    path("delete/<int:rest_id>/", views.delete, name="restaurant_delete"),
    path("register/", views.register_user, name="register"),
    path("login/", views.login_user, name="login"),
    path("logout/", views.logout_user, name="logout"),
    path("create_item/<int:rest_id>/", views.create_item, name="create_item"),
    path("favorite/<int:rest_id>/", views.favorite, name="favorite"),
    path("list/", RestaurantListAPIView.as_view()),
    path("detail/<int:rest_id>/", RestaurantDetailAPIView.as_view()),
    path("deleteit/<int:rest_id>/", RestaurantDeleteAPIView.as_view() ),
    path("createit/", RestaurantCreateAPIView.as_view() ),
    path("updateit/<int:rest_id>/", RestaurantUpdateAPIView.as_view() ),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
