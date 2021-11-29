from django.contrib import admin
from .models import Meals, Category
# Register your models here.

class MealsAdmin(admin.ModelAdmin):
    list_display = ["name", "price"]
    search_fields = ["name", "description"]
    list_filter = ["category", ]

admin.site.register(Meals, MealsAdmin)
admin.site.register(Category)