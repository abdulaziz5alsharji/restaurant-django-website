from django.db import models

# Create your models here.

class WhyChooseUs(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = "why choose us"
        verbose_name_plural = "why choose us"


class Chef(models.Model):
    name = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    bio = models.TextField()
    image = models.ImageField(upload_to="chef/")

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "chef"
        verbose_name_plural = "chefs"