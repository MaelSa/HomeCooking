from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
import datetime
from django.utils.safestring import mark_safe
from django.utils import timezone
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import FormMixin
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView, TemplateView, ListView, DetailView, UpdateView, DeleteView
from .models import RecipeTry, Recipe, Comment, Unit, Ingredient, IngredientInRecipe
import requests
from functools import reduce
import urllib
import operator
from django.contrib import messages


# Create your views here.
def home(request):

    return render(request, 'cookingapp/home.html')

class CreateRecipe(CreateView):
    model = Recipe
    success_url = reverse_lazy('home')