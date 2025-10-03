from django.urls import path
from .views import (
    IngredientListCreateView, IngredientDetailView,
    RecipeListCreateView, RecipeDetailView
)

urlpatterns = [
    # Ingredients
    path('ingredients/', IngredientListCreateView.as_view(), name='ingredient-list'),
    path('ingredients/<int:pk>/', IngredientDetailView.as_view(), name='ingredient-detail'),

    # Recipes
    path('recipes/', RecipeListCreateView.as_view(), name='recipe-list'),
    path('recipes/<int:pk>/', RecipeDetailView.as_view(), name='recipe-detail'),
]
