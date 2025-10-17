from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import IngredientViewSet, RecipeViewSet, RecipeSuggestView

router = DefaultRouter()
router.register(r'ingredients', IngredientViewSet, basename='ingredient')
router.register(r'recipes', RecipeViewSet, basename='recipe')

urlpatterns = [
    # Router URLs
    path('', include(router.urls)),

    # Suggest recipes endpoint
    path('suggest/', RecipeSuggestView.as_view(), name='recipe-suggest'),
]
