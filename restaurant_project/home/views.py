from django.shortcuts import render
from meals.models import Meals, Category
from blog.models import Post
from about.models import WhyChooseUs
# Create your views here.

def home(request):
    meals = Meals.objects.all()
    categories = Category.objects.all()
    posts = Post.objects.all()
    last_post = Post.objects.last()
    why_choose_us = WhyChooseUs.objects.all()
    return render(request, "home/index.html", context={
        "meals": meals,
        "categories": categories,
        "posts": posts,
        "last_post": last_post,
        "why_choose_us": why_choose_us,
    })