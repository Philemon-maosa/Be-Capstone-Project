from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import (
    IngredientListCreateView, IngredientDetailView,
    RecipeListCreateView, IngredientViewSet, RecipeViewSet, RecipeSuggestView, RecipeDetailView
)
router = DefaultRouter()
router.register(r'ingredients', IngredientViewSet, basename='ingredient')
router.register(r'recipes', RecipeViewSet, basename='recipe')


urlpatterns = [
    # Ingredients
    path('ingredients/', IngredientListCreateView.as_view(), name='ingredient-list'),
    path('ingredients/<int:pk>/', IngredientDetailView.as_view(), name='ingredient-detail'),

    # Recipes
    path('recipes/', RecipeListCreateView.as_view(), name='recipe-list'),
    path('recipes/<int:pk>/', RecipeDetailView.as_view(), name='recipe-detail'),
    path('recipes/suggest/', RecipeSuggestView.as_view(), name='recipe-suggest'),
    path('', include(router.urls)),
]
