from django.shortcuts import render
from rest_framework import generics, permissions
from .models import KitchenList
from .serializers import KitchenListSerializer

class KitchenListView(generics.ListCreateAPIView):
    serializer_class = KitchenListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return KitchenList.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class KitchenListDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = KitchenListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return KitchenList.objects.filter(user=self.request.user)

