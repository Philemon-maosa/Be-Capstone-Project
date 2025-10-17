from django.db import models
from django.contrib.auth.models import User

class PantryItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="pantry_items")
    name = models.CharField(max_length=100)
    quantity = models.CharField(max_length=50, blank=True, null=True)
    category = models.CharField(max_length=50, blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.user.username})"
