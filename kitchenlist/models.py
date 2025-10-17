from django.db import models
from django.contrib.auth.models import User
from recipes.models import Recipe

class KitchenList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="kitchenlist_items")
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, null=True, blank=True)
    item_name = models.CharField(max_length=100)
    quantity = models.CharField(max_length=50, blank=True)
    is_checked = models.BooleanField(default=False)
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.item_name} ({self.user.username})"
