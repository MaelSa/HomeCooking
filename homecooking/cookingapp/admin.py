from django.contrib import admin
from .models import Unit, Recipe, RecipeTry, RecipeStep, Ingredient, IngredientInRecipe, Comment


admin.site.register(Recipe)
admin.site.register(RecipeTry)
admin.site.register(Unit)
admin.site.register(IngredientInRecipe)
admin.site.register(Ingredient)
# Register your models here.