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

    def __str__(self):
        return self.date

class Ingredient(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

