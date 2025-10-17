from rest_framework import generics, permissions
from .models import PantryItem
from .serializers import PantryItemSerializer

#  List all pantry items for the logged-in user & create new items
class PantryListCreateView(generics.ListCreateAPIView):
    serializer_class = PantryItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return PantryItem.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Automatically assign the logged-in user
        serializer.save()

#  Retrieve, update, or delete a single pantry item
class PantryDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PantryItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Ensure users only access their own pantry items
        return PantryItem.objects.filter(user=self.request.user)
