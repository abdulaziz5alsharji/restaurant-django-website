from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from taggit.managers import TaggableManager
# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self) -> str:
        return self.category_name


class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="blog", blank=True, null=True)
    tags = TaggableManager()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    created = models.DateTimeField(default=datetime.now())

    class Meta:
        verbose_name = "post"
        verbose_name_plural = "posts"


    def __str__(self) -> str:
        return self.title



class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    created = models.DateTimeField(default=datetime.now())


    def __str__(self) -> str:
        return self.post.title