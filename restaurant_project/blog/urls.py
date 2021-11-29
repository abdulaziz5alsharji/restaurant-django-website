from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.post_list, name="post_list"),
    path("<int:idd>/", views.post_details, name="post_details"),
    path("tag=<slug:tag>/", views.post_by_tag, name="post_by_tag"),
    path("category=<slug:category>/", views.post_by_category, name="post_by_category"),
]
