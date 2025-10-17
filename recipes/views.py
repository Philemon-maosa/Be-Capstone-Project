from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Ingredient, Recipe
from .serializers import IngredientSerializer, RecipeSerializer

# ==============================
# Ingredient ViewSet (CRUD)
# ==============================
class IngredientViewSet(viewsets.ModelViewSet):
    serializer_class = IngredientSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Only show ingredients owned by the logged-in user
        return Ingredient.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

# ==============================
# Recipe ViewSet (CRUD)
# ==============================
class RecipeViewSet(viewsets.ModelViewSet):
    serializer_class = RecipeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Only show recipes owned by the logged-in user
        return Recipe.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save()

# ==============================
# Recipe Suggestion View
# ==============================
class RecipeSuggestView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        """
        Suggest recipes based on provided or saved ingredients.
        Accepts JSON body: {"ingredients": ["tomato", "onion", ...]}
        """
        user_ingredients = request.data.get("ingredients", [])

        # Fallback: use ingredients from DB if none provided
        if not user_ingredients:
            user_ingredients = list(
                Ingredient.objects.filter(owner=request.user).values_list("name", flat=True)
            )

        if not user_ingredients:
            return Response(
                {"error": "No ingredients found. Please add or provide ingredients."},
                status=status.HTTP_400_BAD_REQUEST
            )

        user_ingredients_lower = [i.lower() for i in user_ingredients]
        suggestions = []

        # Only consider recipes owned by the logged-in user
        for recipe in Recipe.objects.filter(owner=request.user):
            recipe_ingredients = [i.name.lower() for i in recipe.ingredients.all()]
            matches = [i for i in user_ingredients_lower if i in recipe_ingredients]
            match_percent = (len(matches) / len(recipe_ingredients)) * 100 if recipe_ingredients else 0
            missing_ingredients = [i for i in recipe_ingredients if i not in user_ingredients_lower]

            suggestions.append({
                "recipe": recipe.name,
                "match_percent": round(match_percent, 2),
                "missing_ingredients": missing_ingredients,
                "instructions": recipe.instructions
            })

        # Sort by best match
        suggestions.sort(key=lambda x: x["match_percent"], reverse=True)
        return Response(suggestions, status=status.HTTP_200_OK)
