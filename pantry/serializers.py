from rest_framework import serializers
from .models import PantryItem

class PantryItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = PantryItem
        fields = '__all__'
        read_only_fields = ['user', 'date_added']

    def create(self, validated_data):
        # Assign the currently logged-in user automatically
        user = self.context['request'].user
        return PantryItem.objects.create(user=user, **validated_data)
