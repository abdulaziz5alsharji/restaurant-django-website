from . import views
from django.urls import path

app_name = "meals"

urlpatterns = [
    path("", views.meal_list, name="meal_list"),
    path("<str:slug>/", views.meal_detail, name="meal_detail"),
]