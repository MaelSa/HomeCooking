from django import forms
from .models import RecipeTry, Recipe, Comment, IngredientInRecipe, Ingredient, Unit

class CreateRecipeForm(forms.ModelForm):

    class Meta:
        model = Recipe
        fields = ('name')

        labels = {
            'name' : ('Nom de la recette')
        }


class CreateIngredient(forms.ModelForm):

    class Meta:
        model = Recipe
        fields = ('name')

        labels = {
            'name': ("Nom de l'ingrédient")
        }


