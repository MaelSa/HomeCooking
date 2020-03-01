from django.db import models
from django.utils import timezone
from django.contrib.auth.models import UserManager, User
from django.contrib.auth import authenticate
import datetime
# Create your models here.

class Recipe(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class RecipeTry(models.Model):
    date = models.DateField(default=timezone.now)
    author = models.CharField(max_length=200)
    comment = models.TextField(max_length=1000)
    grade = models.IntegerField()
    servings = models.IntegerField()

    def __str__(self):
        return self.date

class Ingredient(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Unit(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class RecipeStep(models.Model):
    recipe = models.ForeignKey(RecipeTry, related_name='recipe', on_delete=models.CASCADE)
    stepNumper = models.IntegerField()
    stepText = models.TextField(max_length=1000)

    def __str__(self):
        return self.stepText

class IngredientInRecipe(models.Model):
    ingredient = models.ForeignKey(Ingredient, related_name="ingredient", on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, related_name='recipe', on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit, related_name='unit', on_delete=models.CASCADE)
    quantity = models.IntegerField()


    def __str__(self):
        return self.ingredient.name

class Comment(models.Model):
    recipe = models.ForeignKey(RecipeTry, related_name='recipeTry', on_delete=models.CASCADE)
    author = models.CharField(max_length=50)
    grade = models.IntegerField()
    content = models.TextField(max_length = 1000)
