from django.shortcuts import render
from django.http import Http404
from .models import Meals, Category
# Create your views here.

def meal_list(request):
    meals = Meals.objects.all()
    categories = Category.objects.all()
    return render(request, "meals/list.html", context={
        "meals": meals,
        "categories": categories,
    })



def meal_detail(request, slug):
    meal_details = Meals.objects.get(slug=slug)
    return render(request, "meals/detail.html", context={
        "meal_details": meal_details
    })

