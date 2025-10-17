from django.urls import path
from .views import PantryListCreateView, PantryDetailView

urlpatterns = [
    # List all pantry items & create new
    path('', PantryListCreateView.as_view(), name='pantry-list-create'),

    # Retrieve, update, delete a single pantry item
    path('<int:pk>/', PantryDetailView.as_view(), name='pantry-detail'),
]
