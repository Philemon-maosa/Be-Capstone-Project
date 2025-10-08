# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=100)
    quantity= models.CharField(max_length=50, blank=True, null=True)
    instructions = models.TextField()
    ingredients = models.ManyToManyField("ingredients.Ingredient", related_name="recipes")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="ingredients")

    def __str__(self):
        return f"{self.name} ({self.quantity or ''} {self.unit or ''})"
