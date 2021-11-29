from django.shortcuts import render
from . models import Chef, WhyChooseUs
# Create your views here.

def about(request):
    chefs = Chef.objects.all()
    why_choose_us = WhyChooseUs.objects.all()
    return render(request, "about/about.html", context={
        "chefs": chefs,
        "why_choose_us": why_choose_us,
    })